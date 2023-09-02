import os

from psycopg2 import connect, OperationalError

class Connect:
    @staticmethod
    def create_connection():
        try:
            new_connection = connect(
                host=os.environ.get("HOST"),
                dbname=os.environ.get("DBNAME"),
                user=os.environ.get("USER"),
                password=os.environ.get("PASSWORD"),
                port=os.environ.get("PORT")
            )
            return new_connection
        except OperationalError as error:
            raise OperationalError("Could not connect to database")

    connection = create_connection()
    print(connection)
    