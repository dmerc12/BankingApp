import datetime

from BankingApp.DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from BankingApp.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation

customer_dao = CustomerDALImplementation()
account_dao = BankAccountDALImplementation()
transaction_dao = TransactionDALImplementation()
session_dao = SessionDALImplementation()

def reset_database():
    # reset customer table and populating test customers
    truncate_customer_table = "truncate table banking.customers restart identity cascade;"
    test_customer1 = "insert into banking.customers values (-2, 'test', 'customer', 'money', 'no@money.com', " \
                     "'123-456-7890', '123 This Street, City, State, ZIP');"
    test_customer2 = "insert into banking.customers values (-1, 'test', 'customer', 'work', 'test@email.com', " \
                     "'123-456-7890', '123 This Street, City, State, ZIP');"
    test_customer3 = "insert into banking.customers values (-3, 'no', 'accounts', 'no', 'no@accounts.com', " \
                     "'123-456-7980', '123 That St, City, State, ZIP');"
    customer_dao.access_customer_table(truncate_customer_table)
    customer_dao.access_customer_table(test_customer1)
    customer_dao.access_customer_table(test_customer2)
    customer_dao.access_customer_table(test_customer3)

    # reset bank account table and populate test bank accounts
    truncate_bank_account_table = "truncate table banking.bank_accounts restart identity cascade;"
    test_account1 = "insert into banking.bank_accounts values (-1, -1, 1.00);"
    test_account2 = "insert into banking.bank_accounts values (-2, -1, 5000.00);"
    test_account3 = "insert into banking.bank_accounts values (-3, -1, 50.00);"
    test_account4 = "insert into banking.bank_accounts values (-4, -2, 50.00);"
    account_dao.access_bank_account_table(truncate_bank_account_table)
    account_dao.access_bank_account_table(test_account1)
    account_dao.access_bank_account_table(test_account2)
    account_dao.access_bank_account_table(test_account3)
    account_dao.access_bank_account_table(test_account4)

    # reset transaction table and populate test transaction
    truncate_transaction_table = "truncate table banking.transactions restart identity cascade;"
    test_transaction = "insert into banking.transactions values (-1, 'that one time', 'deposit', -1, 1.00);"
    transaction_dao.access_transaction_table(truncate_transaction_table)
    transaction_dao.access_transaction_table(test_transaction)

    # reset session table and populate test session
    truncate_session_table = "truncate table banking.sessions restart identity cascade;"
    test_session1 = f"insert into banking.sessions values (-1, -1, " \
                    f"'{datetime.datetime.now() + datetime.timedelta(minutes=3)}');"
    test_session2 = f"insert into banking.sessions values (-2, -1, " \
                    f"'{datetime.datetime.now() - datetime.timedelta(days=300)}');"
    session_dao.access_session_table(truncate_session_table)
    session_dao.access_session_table(test_session1)
    session_dao.access_session_table(test_session2)


reset_database()
