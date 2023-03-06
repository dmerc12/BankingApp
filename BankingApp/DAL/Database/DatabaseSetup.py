import datetime

from BankingApp.DAL.BankAccountDAL.BankAccountDALImplementation import BankAccountDALImplementation
from BankingApp.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.DAL.TransactionDAL.TransactionDALImplementation import TransactionDALImplementation

customer_dao = CustomerDALImplementation()
account_dao = BankAccountDALImplementation()
transaction_dao = TransactionDALImplementation()
session_dao = SessionDALImplementation()

def database_setup():
    # customer table setup and populating test customers
    customer_table = "create table banking.customers(customer_id serial primary key, first_name varchar(36), " \
                     "last_name varchar(36), passwrd varchar(60), email varchar(60), phone_number varchar(13), " \
                     "address varchar(60));"
    test_customer1 = "insert into banking.customers values (-2, 'test', 'customer', 'money', 'no@money.com', " \
                     "'123-456-7890', '123 This Street, City, State, ZIP');"
    test_customer2 = "insert into banking.customers values (-1, 'test', 'customer', 'work', 'test@email.com', " \
                     "'123-456-7890', '123 This Street, City, State, ZIP');"
    test_customer3 = "insert into banking.customers values (-3, 'no', 'accounts', 'no', 'no@accounts.com', " \
                     "'123-456-7980', '123 That St, City, State, ZIP');"
    customer_dao.access_customer_table(customer_table)
    customer_dao.access_customer_table(test_customer1)
    customer_dao.access_customer_table(test_customer2)
    customer_dao.access_customer_table(test_customer3)

    # bank account table setup and populate test accounts
    bank_account_table = "create table banking.bank_accounts(account_id serial primary key, customer_id int, " \
                         "balance float check (0 <= balance), constraint customerfk foreign key (customer_id) " \
                         "references Banking.customers(customer_id));"
    test_account1 = "insert into banking.bank_accounts values (-1, -1, 1.00);"
    test_account2 = "insert into banking.bank_accounts values (-2, -1, 5000.00);"
    test_account3 = "insert into banking.bank_accounts values (-3, -1, 50.00);"
    test_account4 = "insert into banking.bank_accounts values (-4, -2, 50.00);"
    account_dao.access_bank_account_table(bank_account_table)
    account_dao.access_bank_account_table(test_account1)
    account_dao.access_bank_account_table(test_account2)
    account_dao.access_bank_account_table(test_account3)
    account_dao.access_bank_account_table(test_account4)

    # transaction table setup and populate test transaction
    transaction_table = "create table banking.transactions(transaction_id serial primary key, time_and_date " \
                        "varchar(26), transaction_type varchar(16), account_id int, amount float, constraint " \
                        "accountfk foreign key (account_id) references Banking.bank_accounts(account_id));"
    test_transaction = "insert into banking.transactions values (-1, 'that one time', 'deposit', -1, 1.00);"
    transaction_dao.access_transaction_table(transaction_table)
    transaction_dao.access_transaction_table(test_transaction)

    # session table setup and populate test session
    session_table = "create table banking.sessions(session_id serial primary key, customer_id int, issue_date_time " \
                    "varchar(26), expire_date_time varchar(26), constraint customerfk foreign key (customer_id) " \
                    "references Banking.customers(customer_id));"
    test_session = f"insert into banking.sessions values (-1, -1, '{datetime.datetime.now()}', " \
                   f"'{datetime.datetime.now()}');"
    session_dao.access_session_table(session_table)
    session_dao.access_session_table(test_session)

database_setup()
