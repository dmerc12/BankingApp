from abc import ABC, abstractmethod

from Entities.Session import Session


class SessionDALInterface(ABC):

    @abstractmethod
    def create_session(self, session: Session) -> Session:
        pass

    @abstractmethod
    def get_session(self, session_id: int) -> Session:
        pass

    @abstractmethod
    def delete_session(self, session_id) -> bool:
        pass