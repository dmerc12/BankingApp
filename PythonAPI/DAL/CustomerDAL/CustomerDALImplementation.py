import logging

from PythonAPI.DAL.CustomerDAL.CustomerDALInterface import CustomerDALInterface
from PythonAPI.DAL.DBConnection import connection
from PythonAPI.Entities.Customer import Customer
from PythonAPI.Entities.FailedTransaction import FailedTransaction


class CustomerDALImplementation(CustomerDALInterface):

    @staticmethod
    def truncate_customer_table(sql_query: str) -> bool:
        cursor = connection.cursor()
        cursor.execute(sql_query)
        connection.commit()
        return True

    @staticmethod
    def populate_test_customer(sql_query: str) -> bool:
        cursor = connection.cursor()
        cursor.execute(sql_query)
        connection.commit()
        return True

    def create_customer(self, customer: Customer) -> Customer:
        logging.info("Beginning DAL method create customer")
        sql = "insert into banking.customers values (default, %s, %s, %s, %s, %s, %s, %s) returning customer_id;"
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name, customer.last_name, customer.username, customer.password,
                             customer.email, customer.phone_number, customer.address))
        connection.commit()
        customer_id = cursor.fetchone()[0]
        customer.customer_id = customer_id
        logging.info("Finishing DAL method create customer")
        return customer

    def get_customer_by_id(self, customer_id: int) -> Customer:
        logging.info("Beginning DAL method get customer by ID")
        sql = "select * from banking.customers where customer_id=%s;"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        customer_info = cursor.fetchone()
        if customer_info is None:
            logging.warning("DAL method get customer by ID, cannot find customer")
            raise FailedTransaction("This customer cannot be found, please try again!")
        customer = Customer(*customer_info)
        logging.info("Finishing DAL method get customer by ID")
        return customer

    def login(self, username: str, password: str) -> Customer:
        logging.info("Beginning DAL method login")
        sql = "select * from banking.customers where username=%s and passwrd=%s;"
        cursor = connection.cursor()
        cursor.execute(sql, (username, password))
        connection.commit()
        customer_info = cursor.fetchone()
        if customer_info is None:
            logging.warning("DAL method login, cannot validate credentials")
            raise FailedTransaction("Either the username or password are incorrect, please try again!")
        customer = Customer(*customer_info)
        logging.info("Finishing DAL method login")
        return customer

    def update_customer(self, customer: Customer) -> Customer:
        logging.info("Beginning DAL method update customer")
        sql = "update banking.customers set first_name=%s, last_name=%s, username=%s, " \
              "passwrd=%s, email=%s, phone_number=%s, address=%s where customer_id=%s;"
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name, customer.last_name, customer.username, customer.password,
                             customer.email, customer.phone_number, customer.address, customer.customer_id))
        connection.commit()
        logging.info("Finishing DAL method update customer")
        return customer

    def delete_customer(self, customer_id: int) -> bool:
        logging.info("Beginning DAL method delete customer")
        sql = "delete from banking.customers where customer_id=%s;"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        logging.info("Finishing DAL method delete customer")
        return True