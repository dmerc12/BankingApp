import logging

from DAL.DBConnection import connection
from DAL.SessionDAL.SessionDALInterface import SessionDALInterface
from Entities.FailedTransaction import FailedTransaction
from Entities.Session import Session


class SessionDALImplementation(SessionDALInterface):

    @staticmethod
    def truncate_session_table(sql_query: str) -> bool:
        cursor = connection.cursor()
        cursor.execute(sql_query)
        connection.commit()
        return True

    @staticmethod
    def populate_expired_test_session(sql_query: str) -> bool:
        cursor = connection.cursor()
        cursor.execute(sql_query)
        connection.commit()
        return True

    def create_session(self, session: Session) -> Session:
        logging.info("Beginning DAL method create session")
        sql = "insert into banking.sessions values (default, %s, %s, %s) returning session_id;"
        cursor = connection.cursor()
        cursor.execute(sql, (session.customer_id, session.issue_date_time, session.expire_date_time))
        connection.commit()
        session_id = cursor.fetchone()[0]
        session.session_id = session_id
        logging.info("Finishing DAL method create session")
        return session

    def get_session(self, session_id: int) -> Session:
        logging.info("Beginning DAL method get session")
        sql = "select * from banking.sessions where session_id=%s;"
        cursor = connection.cursor()
        cursor.execute(sql, [session_id])
        session_info = cursor.fetchone()
        if session_info is None:
            logging.warning("DAL method get session, no session found")
            raise FailedTransaction("No session found, please try again!")
        session = Session(*session_info)
        logging.info("Finishing DAL method get session")
        return session

    def delete_session(self, session_id) -> bool:
        logging.info("Beginning DAL method delete session")
        sql = "delete from banking.sessions where session_id=%s;"
        cursor = connection.cursor()
        cursor.execute(sql, [session_id])
        connection.commit()
        logging.info("Finishing DAL method delete session")
        return True

    def delete_all_sessions(self, customer_id: int) -> bool:
        logging.info("Beginning DAL method delete all sessions")
        sql = "delete from banking.sessions where customer_id=%s;"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        logging.info("Finishing DAL method delete all sessions")
        return True
