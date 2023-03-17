from BankingApp.DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from BankingApp.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation

customer_dao = CustomerDALImplementation()
account_dao = BankAccountDALImplementation()
transaction_dao = TransactionDALImplementation()
session_dao = SessionDALImplementation()

def drop_database():
    # drop transaction table
    drop_transaction_table = "drop table banking.transactions;"
    transaction_dao.access_transaction_table(drop_transaction_table)

    # drop session table
    drop_session_table = "drop table banking.sessions;"
    session_dao.access_session_table(drop_session_table)

    # drop bank account table
    drop_bank_account_table = "drop table banking.bank_accounts;"
    account_dao.access_bank_account_table(drop_bank_account_table)

    # drop customer table
    drop_customer_table = "drop table banking.customers;"
    customer_dao.access_customer_table(drop_customer_table)

    # drop banking schema
    drop_banking_schema = "drop schema banking"
    customer_dao.access_customer_table(drop_banking_schema)

drop_database()
