from datetime import datetime, timedelta

from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.Entities.Session import Session

session_dao = SessionDALImplementation()
session_expire_time = str(datetime.now() + timedelta(0, 0, 0, 0, 30))
test_session = Session(0, -1, session_expire_time)
update_session = Session(test_session.session_id, test_session.customer_id, session_expire_time)

def test_create_session_success():
    result = session_dao.create_session(test_session)
    assert result.session_id != 0

def test_get_session_success():
    result = session_dao.get_session(test_session.session_id)
    assert result is not None

def test_update_session_success():
    result = session_dao.update_session(update_session)
    assert result.session_id == update_session.session_id and result.customer_id == update_session.customer_id and\
           result.expire_date_time == update_session.expire_date_time

def test_delete_session_success():
    result = session_dao.delete_session(test_session.session_id)
    assert result
