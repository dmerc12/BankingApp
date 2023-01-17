import logging

from DAL.DBConnection import connection
from DAL.SessionDAL.SessionDALInterface import SessionDALInterface
from Entities.Session import Session


class SessionDALImplementation(SessionDALInterface):

    @staticmethod
    def truncate_session_table(sql_query: str) -> bool:
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
        pass

    def delete_session(self, session_id) -> bool:
        pass
