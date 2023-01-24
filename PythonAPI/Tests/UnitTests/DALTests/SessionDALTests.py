from datetime import datetime

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from Entities.Session import Session

session_dao = SessionDALImplementation()
session_start_date = datetime.now()
session_expire_time = session_start_date.minute + 30
test_session = Session(0, -1, str(session_start_date), str(session_expire_time))

def test_create_session_success():
    result = session_dao.create_session(test_session)
    assert result.session_id != 0

def test_get_session_success():
    result = session_dao.get_session(test_session.session_id)
    assert result is not None

def test_delete_session_success():
    result = session_dao.delete_session(test_session.session_id)
    assert result
