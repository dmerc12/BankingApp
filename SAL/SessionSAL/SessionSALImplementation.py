from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from Entities.Session import Session
from SAL.SessionSAL.SessionSALInterface import SessionSALInterface


class SessionSALImplementation(SessionSALInterface):

    def __init__(self, session_dao: SessionDALImplementation):
        self.session_dao = session_dao

    def service_create_session(self, session: Session) -> Session:
        pass

    def service_get_session(self, session_id: int) -> Session:
        pass

    def service_delete_session(self, session_id: int) -> bool:
        pass
