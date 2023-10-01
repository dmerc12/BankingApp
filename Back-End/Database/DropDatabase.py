from Database.config import Connect

def drop_database():
    cursor = Connect.connection.cursor()

    # drop session table
    drop_session_table = "drop table banking.sessions;"
    cursor.execute(drop_session_table)

    # drop bank account table
    drop_bank_account_table = "drop table banking.bank_accounts;"
    cursor.execute(drop_bank_account_table)

    # drop customer table
    drop_customer_table = "drop table banking.customers;"
    cursor.execute(drop_customer_table)

    # drop banking schema
    drop_banking_schema = "drop schema banking"
    cursor.execute(drop_banking_schema)

    Connect.connection.commit()

drop_database()
