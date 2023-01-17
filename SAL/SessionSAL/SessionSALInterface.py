from abc import ABC, abstractmethod
from Entities.Session import Session


class SessionSALInterface(ABC):

    @abstractmethod
    def service_create_session(self, session: Session) -> Session:
        pass

    @abstractmethod
    def service_get_session(self, session_id: int) -> Session:
        pass

    @abstractmethod
    def service_delete_session(self, session_id: int) -> bool:
        pass
