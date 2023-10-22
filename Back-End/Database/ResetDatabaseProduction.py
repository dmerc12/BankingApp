from Database.config import Connect

def reset_database():
    cursor = Connect.connection.cursor()

    # reset customer table
    truncate_customer_table = "truncate table banking.customers restart identity cascade;"
    cursor.execute(truncate_customer_table)

    # reset bank account table
    truncate_bank_account_table = "truncate table banking.bank_accounts restart identity cascade;"
    cursor.execute(truncate_bank_account_table)

    # reset session table
    truncate_session_table = "truncate table banking.sessions restart identity cascade;"
    cursor.execute(truncate_session_table)

    Connect.connection.commit()

reset_database()
