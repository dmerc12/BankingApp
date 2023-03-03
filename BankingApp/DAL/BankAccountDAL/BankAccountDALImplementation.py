import logging
from typing import List
from BankingApp.DAL.BankAccountDAL.BankAccountDALInterface import BankAccountDALInterface
from BankingApp.DAL.Database.config import Connect
from BankingApp.Entities.BankAccount import BankAccount
from BankingApp.Entities.FailedTransaction import FailedTransaction


class BankAccountDALImplementation(BankAccountDALInterface):

    @staticmethod
    def access_bank_account_table(sql_query: str) -> bool:
        cursor = Connect.connection.cursor()
        cursor.execute(sql_query)
        Connect.connection.commit()
        return True

    def create_account(self, account: BankAccount) -> BankAccount:
        logging.info("Beginning DAL method create account")
        sql = "insert into banking.bank_accounts values (default, %s, %s) returning account_id;"
        cursor = Connect.connection.cursor()
        cursor.execute(sql, (account.customer_id, account.balance))
        Connect.connection.commit()
        account_id = cursor.fetchone()[0]
        account.account_id = account_id
        logging.info("Finishing DAL method create account")
        return account

    def get_account_by_id(self, account_id: int) -> BankAccount:
        logging.info("Beginning DAL method get account by ID")
        sql = "select * from banking.bank_accounts where account_id=%s;"
        cursor = Connect.connection.cursor()
        cursor.execute(sql, [account_id])
        account_info = cursor.fetchone()
        if account_info is None:
            logging.warning("DAL method get account by ID, account not found")
            raise FailedTransaction("This account cannot be found, please try again!")
        account = BankAccount(*account_info)
        logging.info("Finishing DAL method get account by ID")
        return account

    def get_all_accounts(self, customer_id: int) -> List[BankAccount]:
        logging.info("Beginning DAL method get all accounts")
        sql = "select * from banking.bank_accounts where customer_id=%s;"
        cursor = Connect.connection.cursor()
        cursor.execute(sql, [customer_id])
        account_records = cursor.fetchall()
        account_list = []
        for account in account_records:
            account = BankAccount(*account)
            account_list.append(account)
        if len(account_list) == 0:
            logging.warning("DAL method get all accounts, no accounts found")
            raise FailedTransaction("No accounts found, please try again!")
        else:
            logging.info("Finishing DAL method get all accounts")
            return account_list

    def deposit(self, account_id: int, deposit_amount: float) -> BankAccount:
        logging.info("Beginning DAL method deposit")
        sql = "update banking.bank_accounts set balance=%s where account_id=%s returning *;"
        cursor = Connect.connection.cursor()
        current_balance = self.get_account_by_id(account_id).balance
        new_balance = current_balance + deposit_amount
        cursor.execute(sql, (new_balance, account_id))
        Connect.connection.commit()
        updated_info = cursor.fetchone()
        updated_account = BankAccount(*updated_info)
        logging.info("Finishing DAL method deposit")
        return updated_account

    def withdraw(self, account_id: int, withdraw_amount: float) -> BankAccount:
        logging.info("Beginning DAL method withdraw")
        sql = "update banking.bank_accounts set balance=%s where account_id=%s returning *;"
        cursor = Connect.connection.cursor()
        current_balance = self.get_account_by_id(account_id).balance
        new_balance = current_balance - withdraw_amount
        cursor.execute(sql, (new_balance, account_id))
        Connect.connection.commit()
        updated_info = cursor.fetchone()
        updated_account = BankAccount(*updated_info)
        logging.info("Finishing DAL method withdraw")
        return updated_account

    def transfer(self, withdraw_account_id: int, deposit_account_id: int, transfer_amount: float) -> bool:
        logging.info("Beginning DAL method transfer")
        sql1 = "update banking.bank_accounts set balance=(balance - %s) where account_id=%s;"
        sql2 = "update banking.bank_accounts set balance=(balance + %s) where account_id=%s;"
        cursor = Connect.connection.cursor()
        cursor.execute(sql1, (transfer_amount, withdraw_account_id))
        cursor.execute(sql2, (transfer_amount, deposit_account_id))
        Connect.connection.commit()
        logging.info("Finishing DAL method transfer")
        return True

    def delete_account(self, account_id: int) -> bool:
        logging.info("Beginning DAL method delete account")
        sql = "delete from banking.bank_accounts where account_id=%s;"
        cursor = Connect.connection.cursor()
        cursor.execute(sql, [account_id])
        Connect.connection.commit()
        logging.info("Finishing DAL method delete account")
        return True
