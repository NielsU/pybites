from db_intro import DB, SQLiteType, SchemaError
from sqlite3 import Cursor
from enum import Enum

schema = [("description", SQLiteType.TEXT), ("id", SQLiteType.INTEGER)]

# """
# SELECT name, sql
# FROM sqlite_master
# WHERE type = 'table'
# """

# db.cursor.execute(
#     """
# SELECT name, sql
# FROM sqlite_master
# """
# )


def get_schema(curs: Cursor, tablename: str) -> dict[str, Enum]:
    curs.execute(str.format("PRAGMA table_info({0})", tablename))
    table_info = curs.fetchall()
    column_dict = {item[1]: SQLiteType._member_map_[item[2]] for item in table_info}
    return column_dict


with DB() as db:
    db.create("product", schema, "id")
    db.cursor.execute("PRAGMA table_info(product)")

    result = db.cursor.fetchall()

    schema_dict = get_schema(db.cursor, "product")

    print(schema_dict)

# print(SQLiteType._member_map_["TEXT"])
