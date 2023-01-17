from datetime import datetime

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from Entities.Session import Session
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)
session_start = datetime.now()
session_expire = session_start.minute + 30
successful_session = Session(0, -1, str(session_start), str(session_expire))

def test_service_create_session_customer_id_not_integer():
    pass

def test_service_create_session_customer_not_found():
    pass

def test_service_create_session_issue_date_time_not_string():
    pass

def test_service_create_session_issue_date_time_too_long():
    pass

def test_service_create_session_issue_date_time_empty():
    pass

def test_service_create_session_expire_date_time_not_string():
    pass

def test_service_create_session_expire_date_time_too_long():
    pass

def test_service_create_session_expire_date_time_empty():
    pass

def test_service_create_session_success():
    pass

def test_service_get_session_id_not_integer():
    pass

def test_service_get_session_not_found():
    pass

def test_service_get_session_expired():
    pass

def test_service_get_session_success():
    pass

def test_service_delete_session_id_not_integer():
    pass

def test_service_delete_session_not_found():
    pass

def test_service_delete_session_success():
    pass
