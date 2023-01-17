import datetime

from DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation

customer_dao = CustomerDALImplementation()
account_dao = BankAccountDALImplementation()
transaction_dao = TransactionDALImplementation()

def reset_database():
    sql1 = "truncate table banking.customers restart identity cascade;"
    sql2 = "truncate table banking.bank_accounts restart identity cascade;"
    sql3 = "truncate table banking.transactions restart identity cascade;"
    sql4 = "truncate table banking.sessions restart identity cascade;"
    sql5 = "insert into banking.customers values (-1, 'test', 'customer', 'please', 'work', 'test@email.com', " \
           "'123-456-7890', '123 This Street, City, State, ZIP');"
    sql6 = "insert into banking.bank_accounts values (-1, -1, 1.00);"
    sql7 = "insert into banking.transactions values (-1, 'that one time', 'deposit', -1, 1.00);"
    customer_dao.truncate_customer_table(sql1)
    customer_dao.populate_test_customer(sql5)
    account_dao.truncate_bank_account_table(sql2)
    account_dao.populate_test_account(sql6)
    transaction_dao.truncate_transaction_table(sql3)
    transaction_dao.populate_transaction_table(sql7)

reset_database()
