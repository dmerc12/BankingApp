import logging
from datetime import datetime

from PythonAPI.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from PythonAPI.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from PythonAPI.Entities.FailedTransaction import FailedTransaction
from PythonAPI.Entities.Session import Session
from PythonAPI.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from PythonAPI.SAL.SessionSAL.SessionSALInterface import SessionSALInterface


class SessionSALImplementation(SessionSALInterface):
    customer_dao = CustomerDALImplementation()
    customer_sao = CustomerSALImplementation(customer_dao)

    def __init__(self, session_dao: SessionDALImplementation):
        self.session_dao = session_dao

    def service_create_session(self, session: Session) -> Session:
        logging.info("Beginning SAL method create session")
        if type(session.customer_id) != int:
            logging.warning("SAL method create session, customer ID not an integer")
            raise FailedTransaction("The customer ID field must be an integer, please try again!")
        elif type(session.issue_date_time) != str:
            logging.warning("SAL method create session, issue date time not a string")
            raise FailedTransaction("The issue date and time field must be a string, please try again!")
        elif type(session.expire_date_time) != str:
            logging.warning("SAL method create session, expire date time not a string")
            raise FailedTransaction("The expire date and time field must be a string, please try again!")
        elif len(session.issue_date_time) > 26:
            logging.warning("SAL method create session, issue date time longer than 26 characters")
            raise FailedTransaction("The issue date and time field cannot exceed 26 characters, please try again!")
        elif len(session.expire_date_time) > 26:
            logging.warning("SAL method create session, expire date time longer than 26 characters")
            raise FailedTransaction("The expire date and time field cannot exceed 26 characters, please try again!")
        elif len(session.issue_date_time) == 0:
            logging.warning("SAL method create session, issue date time left empty")
            raise FailedTransaction("The issue date and time field cannot be left empty, please try again!")
        elif len(session.expire_date_time) == 0:
            logging.warning("SAL method create session, expire date time left empty")
            raise FailedTransaction("The expire date and time field cannot be left empty, please try again!")
        else:
            self.customer_sao.service_get_customer_by_id(session.customer_id)
            new_session = self.session_dao.create_session(session)
            logging.info("Finishing SAL method create session")
            return new_session

    def service_get_session(self, session_id: int) -> Session:
        logging.info("Beginning SAL method get session")
        if type(session_id) != int:
            logging.warning("SAL method get session, session ID not an integer")
            raise FailedTransaction("The session ID field must be an integer, please try again!")
        else:
            session = self.session_dao.get_session(session_id)
            session_expire_date_time = session.convert_expire_date_time(session)
            if session_expire_date_time < datetime.now():
                logging.warning("SAL method get session, session expired")
                raise FailedTransaction("Session has expired, please log in!")
            else:
                logging.info("Finishing SAL method get session")
                return session

    def service_delete_session(self, session_id: int) -> bool:
        logging.info("Beginning SAL method delete session")
        if type(session_id) != int:
            logging.warning("SAL method delete session, session ID not an integer")
            raise FailedTransaction("The session ID field must be an integer, please try again!")
        else:
            self.session_dao.get_session(session_id)
            self.session_dao.delete_session(session_id)
            logging.info("Finishing SAL method delete session")
            return True

    def service_delete_all_sessions(self, customer_id: int) -> bool:
        logging.info("Beginning SAL method delete all sessions")
        result = self.session_dao.delete_all_sessions(customer_id)
        logging.info("Finishing SAL method delete all sessions")
        return result
