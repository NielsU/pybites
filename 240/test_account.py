from account import Account

import pytest

# write your pytest functions below, they need to start with test_


@pytest.fixture()
def peters_account():
    return Account("Peter", 150000)


@pytest.fixture()
def jullians_account():
    return Account("Julian", 1000000)


@pytest.fixture()
def bobs_account():
    return Account("Bob", 1000000)


def test_init(peters_account):
    assert peters_account.owner == "Peter"
    assert peters_account.amount == 150000

    assert len(peters_account) == 0


def test_init_default_amount():
    assert Account("Mr x").amount == 0


def test_repr(peters_account):
    assert (
        repr(peters_account)
        == f"Account('{peters_account.owner}', {peters_account.amount})"
    )


def test_str(peters_account):
    assert (
        str(peters_account)
        == f"Account of {peters_account.owner} with starting amount: {peters_account.amount}"
    )


def test_equal_accounts(jullians_account, bobs_account):
    assert jullians_account == bobs_account


def test_not_equal_accounts(peters_account, bobs_account):
    assert peters_account != bobs_account


def test_account_peter_lt_bob(peters_account, bobs_account):
    assert peters_account < bobs_account


def test_account_peter_ht_Jim(peters_account, bobs_account):
    assert bobs_account > peters_account


def test_add_transaction_valid():
    amount = 15000
    account = Account("Harry")
    account.add_transaction(amount)

    assert len(account) == 1


def test_add_transaction_value_error():
    amount = "15000"
    account = Account("Harry")
    with pytest.raises(ValueError):
        account.add_transaction(amount)


def test_balance(peters_account):
    transaction_amount = 1500

    peters_account.add_transaction(1500)

    assert peters_account.balance == (transaction_amount + peters_account.amount)


def test_account_get_item(peters_account):
    peters_account.add_transaction(1500)
    peters_account.add_transaction(200)

    assert peters_account[0] == 1500
    assert peters_account[1] == 200


def test_add(jullians_account, bobs_account):
    founders_shared = jullians_account + bobs_account

    assert type(founders_shared) is Account

    assert str(founders_shared) == "Account of Julian&Bob with starting amount: 2000000"


def test_add_with_transactions(peters_account, jullians_account):
    peters_account.add_transaction(100)
    jullians_account.add_transaction(200)

    shared = peters_account + jullians_account

    assert len(shared._transactions) == 2
    assert sum(shared._transactions) == 300
    assert shared.amount == peters_account.amount + jullians_account.amount

    # sum of amounts and transactions of summed accounts.
    assert shared.balance == 1150300

    assert str(shared) == "Account of Peter&Julian with starting amount: 1150000"
