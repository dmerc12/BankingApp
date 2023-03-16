from datetime import datetime, timedelta

from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.Entities.Session import Session

session_dao = SessionDALImplementation()
session_expire_time = datetime.now() + timedelta(0, 0, 0, 0, 30)
test_session = Session(0, -1, str(session_expire_time))

def test_create_session_success():
    result = session_dao.create_session(test_session)
    assert result.session_id != 0

def test_get_session_success():
    result = session_dao.get_session(test_session.session_id)
    assert result is not None

def test_delete_session_success():
    result = session_dao.delete_session(test_session.session_id)
    assert result
