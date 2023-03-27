import datetime

import bcrypt

from BankingApp.DAL.Database.config import Connect

def reset_database():
    cursor = Connect.connection.cursor()

    # reset customer table and populating test customers
    truncate_customer_table = "truncate table banking.customers restart identity cascade;"
    cursor.execute(truncate_customer_table)

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

    # reset bank account table and populate test bank accounts
    truncate_bank_account_table = "truncate table banking.bank_accounts restart identity cascade;"
    cursor.execute(truncate_bank_account_table)

    test_account1 = "insert into banking.bank_accounts values (-1, -1, 1.00);"
    cursor.execute(test_account1)

    test_account2 = "insert into banking.bank_accounts values (-2, -1, 5000.00);"
    cursor.execute(test_account2)

    test_account3 = "insert into banking.bank_accounts values (-3, -1, 50.00);"
    cursor.execute(test_account3)

    test_account4 = "insert into banking.bank_accounts values (-4, -2, 50.00);"
    cursor.execute(test_account4)

    # reset transaction table and populate test transaction
    truncate_transaction_table = "truncate table banking.transactions restart identity cascade;"
    cursor.execute(truncate_transaction_table)

    test_transaction = "insert into banking.transactions values (-1, 'that one time', 'deposit', -1, 1.00);"
    cursor.execute(test_transaction)

    # reset session table and populate test session
    truncate_session_table = "truncate table banking.sessions restart identity cascade;"
    cursor.execute(truncate_session_table)

    test_session1 = f"insert into banking.sessions values (-1, -1, " \
                    f"'{datetime.datetime.now() + datetime.timedelta(minutes=3)}');"
    cursor.execute(test_session1)

    test_session2 = f"insert into banking.sessions values (-2, -1, " \
                    f"'{datetime.datetime.now() - datetime.timedelta(days=300)}');"
    cursor.execute(test_session2)

    Connect.connection.commit()

reset_database()
