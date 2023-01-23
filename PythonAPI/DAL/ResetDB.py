import datetime

from PythonAPI.DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from PythonAPI.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from PythonAPI.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from PythonAPI.DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation

customer_dao = CustomerDALImplementation()
account_dao = BankAccountDALImplementation()
transaction_dao = TransactionDALImplementation()
session_dao = SessionDALImplementation()

def reset_database():
    sql1 = "truncate table banking.customers restart identity cascade;"
    sql2 = "truncate table banking.bank_accounts restart identity cascade;"
    sql3 = "truncate table banking.transactions restart identity cascade;"
    sql4 = "truncate table banking.sessions restart identity cascade;"
    sql5 = "insert into banking.customers values (-1, 'test', 'customer', 'please', 'work', 'test@email.com', " \
           "'123-456-7890', '123 This Street, City, State, ZIP');"
    sql6 = "insert into banking.bank_accounts values (-1, -1, 1.00);"
    sql7 = "insert into banking.transactions values (-1, 'that one time', 'deposit', -1, 1.00);"
    sql8 = f"insert into banking.sessions values (-1, -1, '{datetime.datetime.now()}', '{datetime.datetime.now()}');"
    sql9 = "insert into banking.bank_accounts values (-2, -1, 5000.00);"
    sql10 = "insert into banking.customers values (-2, 'test', 'customer', 'no', 'money', 'no@money.com', " \
            "'123-456-7890', '123 This Street, City, State, ZIP');"
    sql11 = "insert into banking.bank_accounts values (-3, -1, 50.00);"
    customer_dao.truncate_customer_table(sql1)
    customer_dao.populate_test_customer(sql5)
    account_dao.truncate_bank_account_table(sql2)
    session_dao.truncate_session_table(sql4)
    account_dao.populate_test_account(sql6)
    transaction_dao.truncate_transaction_table(sql3)
    transaction_dao.populate_transaction_table(sql7)
    session_dao.populate_expired_test_session(sql8)
    account_dao.populate_test_account(sql9)
    customer_dao.populate_test_customer(sql10)
    account_dao.populate_test_account(sql11)

reset_database()
