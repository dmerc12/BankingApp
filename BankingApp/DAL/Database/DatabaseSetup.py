import datetime

import bcrypt

from BankingApp.DAL.Database.config import Connect

def database_setup():
    cursor = Connect.connection.cursor()

    # creating banking schema
    banking_schema = "create schema banking"
    cursor.execute(banking_schema)

    # customer table setup and populating test customers
    customer_table = "create table banking.customers(customer_id serial primary key, first_name varchar(36), " \
                     "last_name varchar(36), passwrd varchar(60), email varchar(60), phone_number varchar(13), " \
                     "address varchar(60));"
    cursor.execute(customer_table)

    password1 = "money"
    hashed_password1 = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    test_customer1 = "insert into banking.customers values (-2, 'test', 'customer', %s, 'no@money.com', " \
                     "'123-456-7890', '123 This Street, City, State, ZIP');"
    cursor.execute(test_customer1, [hashed_password1])

    password2 = "work"
    hashed_password2 = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    test_customer2 = "insert into banking.customers values (-1, 'test', 'customer', %s, 'test@email.com', " \
                     "'123-456-7890', '123 This Street, City, State, ZIP');"
    cursor.execute(test_customer2, [hashed_password2])

    password3 = "no"
    hashed_password3 = bcrypt.hashpw(password3.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    test_customer3 = "insert into banking.customers values (-3, 'no', 'accounts', %s, 'no@accounts.com', " \
                     "'123-456-7980', '123 That St, City, State, ZIP');".format(hashed_password3)
    cursor.execute(test_customer3, [hashed_password3])

    # bank account table setup and populate test accounts
    bank_account_table = "create table banking.bank_accounts(account_id serial primary key, customer_id int, " \
                         "balance float check (0 <= balance), constraint customerfk foreign key (customer_id) " \
                         "references Banking.customers(customer_id));"
    cursor.execute(bank_account_table)

    test_account1 = "insert into banking.bank_accounts values (-1, -1, 1.00);"
    cursor.execute(test_account1)

    test_account2 = "insert into banking.bank_accounts values (-2, -1, 5000.00);"
    cursor.execute(test_account2)

    test_account3 = "insert into banking.bank_accounts values (-3, -1, 50.00);"
    cursor.execute(test_account3)

    test_account4 = "insert into banking.bank_accounts values (-4, -2, 50.00);"
    cursor.execute(test_account4)

    # transaction table setup and populate test transaction
    transaction_table = "create table banking.transactions(transaction_id serial primary key, time_and_date " \
                        "varchar(26), transaction_type varchar(16), account_id int, amount float, constraint " \
                        "accountfk foreign key (account_id) references Banking.bank_accounts(account_id));"
    cursor.execute(transaction_table)

    test_transaction = "insert into banking.transactions values (-1, 'that one time', 'deposit', -1, 1.00);"
    cursor.execute(test_transaction)

    # session table setup and populate test session
    session_table = "create table banking.sessions(session_id serial primary key, customer_id int, expire_date_time " \
                    "varchar(26), constraint customerfk foreign key (customer_id) " \
                    "references Banking.customers(customer_id));"
    cursor.execute(session_table)

    test_session1 = f"insert into banking.sessions values (-1, -1, " \
                    f"'{datetime.datetime.now() + datetime.timedelta(minutes=3)}');"
    cursor.execute(test_session1)

    test_session2 = f"insert into banking.sessions values (-2, -1, " \
                    f"'{datetime.datetime.now() - datetime.timedelta(days=300)}');"
    cursor.execute(test_session2)

    Connect.connection.commit()

database_setup()
