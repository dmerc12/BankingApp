from DAL.SessionDAL.SessionDALInterface import SessionDALInterface
from Entities.Session import Session


class SessionDALImplementation(SessionDALInterface):
    def create_session(self, session: Session) -> Session:
        pass

    def get_session(self, session_id: int) -> Session:
        pass

    def delete_session(self, session_id) -> bool:
        pass
