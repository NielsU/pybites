import sqlite3
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple, Union


class SQLiteType(Enum):
    """Enum matching SQLite data types to corresponding Python types.

    Supported SQLite types:
        https://docs.python.org/3/library/sqlite3.html#sqlite-and-python-types.

    This Enum is uses in the definition of a table schema to define
        the allowed data type of a column.

    Example: SQLiteType.INTEGER is the ENUM,
        SQLiteType.INTEGER.name is "INTEGER",
        SQLiteType.INTEGER.value is int.
    """

    NULL = None
    INTEGER = int
    REAL = float
    TEXT = str
    BLOB = bytes


class SchemaError(Exception):
    """Base Schema error class if a table schema is not respected."""

    pass


class DB:
    """SQLite Database class.

    Supports all major CRUD operations.
    This DB operates in-memory only by default.

    Attributes:
        location (str): The location of the database.
            Either a .db file or the special :memory: value for an
            in-memory database connection.
        connection (sqlite3.Connection): Connection object used to interact with
            the SQLite database.
        cursor (sqlite3.Cursor): Cursor object used to send SQL statements
            to a SQLite database.
        table_schemas (dict): The table schemas of the database.
            The key is the table name and the value is a list of pairs of
            column name and column type.
    """

    def __init__(self, location: Optional[str] = ":memory:"):
        self.location = location
        self.cursor = None
        self.connection = None
        self.table_schemas = {}
        self._transactions = 0

    def __enter__(self):
        self.connection = sqlite3.connect(self.location)
        self.cursor = self.connection.cursor()

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()

    def _table_schema(self, tablename: str) -> List[Tuple[str, Enum, int]]:
        self.cursor.execute(str.format("PRAGMA table_xinfo({0})", tablename))
        table_info = self.cursor.fetchall()
        return [
            (str(item[1]), SQLiteType._member_map_[item[2]], int(item[-1]))
            for item in table_info
        ]

    def create(
        self, table: str, schema: List[Tuple[str, SQLiteType]], primary_key: str
    ):
        """Creates a new table.

        Makes use of the SQLiteType enum class.
        Updates the table_schemas attribute.

        You can declare any column of the schema to serve as the primary key by adding
            'primary key' after the column name in the SQL statement.

        If the primary key is not part of the schema,
            a SchemaError should be raised with the message:
            "The provided primary key must be part of the schema."

        Args:
            table (str): The table's name.
            schema (list): A list of columns and their SQLite data types.
                Example: [("make", SQLiteType.TEXT), ("year": SQLiteType.INTEGER)].
            primary_key (str): The primary key column of the provided schema.

        Raises:
            SchemaError: If the given primary key is not part of the schema.
        """
        # filter out the schema item matching primary key, if not present raise error
        if len(list(filter(lambda i: i[0] == primary_key, schema))) == 0:
            raise SchemaError("The provided primary key must be part of the schema.")

        # construct sql create statement based on schema
        sql_schema = ""

        for item in schema:
            # ADD COLUMN
            sql_schema += f"{item[0]} {str(item[1].name)}"
            # If indicate primary key
            if item[0] == primary_key:
                sql_schema += " PRIMARY KEY"
            # end line
            sql_schema += ", "

        sql_schema = sql_schema[0:-2]
        full_query = f"CREATE TABLE {table} ( {sql_schema} );"

        # execute table creation
        self.cursor.execute(full_query)

    def delete(self, table: str, target: Tuple[str, Any]):
        """Deletes rows from the table.

        Args:
            table (str): The table's name.
            target (tuple): What to delete from the table. The tuple consists
                of the column name and the actual value. For example, if you
                wanted to remove the row(s) with the year 1999, you would pass it
                ("year", 1999). Only supports "=" operator in this bite.
        """
        raise NotImplementedError("You have to implement this method first.")

    def insert(self, table: str, values: List[Tuple]):
        """Inserts one or multiple new records into the database.

        Before inserting a value, you should make sure
            that the schema for the table is respected.

        If there are more or less values than columns,
            a SchemaError should be raised with the message:
            "Table <table-name> expects items with <table-columns-count> values."

        If the type of a value does not respect the type of the column,
            a SchemaError should be raised with the message:
            "Column <column-name> expects values of type <column-type>."

        To add several values with a single command, you might want to look into
            [executemany](https://docs.python.org/2/library/sqlite3.html#sqlite3.Cursor.executemany)

        Args:
            table (str): The table's name.
            values (list): A list of values to insert.
                Values must respect the table schema.
                The tuple consists of the values for each column in the table.
                Example: [("VW", 2001), ("Tesla", 2020)]

        Raises:
            SchemaError: If a value does not respect the table schema or
                if there are more values than columns for the given table.
        """
        # get table schema:
        table_schema = self._table_schema(table)

        # execute schema validation for each row.
        for row in values:
            # check if number of columns in value row matches schema
            if len(table_schema) != len(row):
                raise SchemaError(
                    f"Table {table} expects items with {len(table_schema)} values."
                )

            # check if colum value type matches the type exected in db column.
            for index, column in enumerate(row):
                if not isinstance(column, table_schema[index][1].value):
                    raise SchemaError(
                        f"Column {table_schema[index][0]} expects values of type {table_schema[index][1].value.__name__}."
                    )

        # execute insert per row (could be changed to execute multiple)
        for row in values:
            # construct sql_snippet for parameter placeholders based on nr of values
            str_columns = "(" + str("?, " * len(row)).rstrip(", ") + ")"

            # construct the insert statement
            sql_statement = f"INSERT INTO {table} VALUES {str_columns}"

            self.cursor.execute(sql_statement, row)

            # update transaction log
            self._transactions += self.cursor.rowcount
        if self.connection.in_transaction:
            self.connection.commit()

    def select(
        self,
        table: str,
        columns: Optional[List[str]] = None,
        target: Optional[Tuple[str, Optional[str], Any]] = None,
    ) -> List[Tuple]:
        """Selects records from the database.

        If there are no columns given, select all available columns as default.

        If a target is given, but no operator (length of target < 3), assume equality check.

        Args:
            table (str): The table's name.
            columns (list, optional): List of the column names that you want to retrieve.
                Defaults to None.
            target (tuple, optional): If you want to narrow down the records returned,
                you can specify the column name, the operator and a value to look for.
                Defaults to None. Example: ("year", 1999) <-> ("year", "=", 1999).

        Returns:
            list: The output returned from the sql command
        """

        # compose columns sql snippit
        sql_columns = ""
        if columns is None or len(columns) < 1:
            sql_columns = " * "
        else:
            sql_columns = ", ".join(columns)

        # compose where clause
        sql_where = ""
        values = []
        if target is not None:
            if len(target) < 3:
                sql_where = f" {target[0]} = ?"
            else:
                sql_where = f" {target[0]} {target[1]} ?"

            values.append(target[-1])
            sql_where = " WHERE " + sql_where

        # construct select statement
        select_statement = f"SELECT {sql_columns} FROM {table}{sql_where}"

        # query and return results
        result = self.cursor.execute(select_statement, values)
        return result.fetchall()

    def update(self, table: str, new_value: Tuple[str, Any], target: Tuple[str, Any]):
        """Update a record in the database.

        Args:
            table (str): The table's name.
            new_value (tuple): The new value that you want to enter. For example,
                if you wanted to change "year" to 2001 you would pass it ("year", 2001).
            target (tuple): The row/record to modify. Example ("year", 1991)
        """
        raise NotImplementedError("You have to implement this method first.")

    @property
    def num_transactions(self) -> int:
        """The total number of changes since the database connection was opened.

        Returns:
            int: Returns the total number of database rows that have been modified.
        """
        return self._transactions
