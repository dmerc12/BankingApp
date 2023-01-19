from datetime import datetime, timedelta
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from Entities.FailedTransaction import FailedTransaction
from Entities.Session import Session
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)
session_start = datetime.now()
session_expire = datetime.now() + timedelta(days=1)
successful_session = Session(0, -1, str(session_start), str(session_expire))

def test_service_create_session_customer_id_not_integer():
    try:
        test_session = Session(0, "-1", str(session_start), str(session_expire))
        session_sao.service_create_session(test_session)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The customer ID field must be an integer, please try again!"

def test_service_create_session_customer_not_found():
    try:
        test_session = Session(0, -50000000, str(session_start), str(session_expire))
        session_sao.service_create_session(test_session)
        assert False
    except FailedTransaction as error:
        assert str(error) == "This customer cannot be found, please try again!"

def test_service_create_session_issue_date_time_not_string():
    try:
        test_session = Session(0, -1, session_start, str(session_expire))
        session_sao.service_create_session(test_session)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The issue date and time field must be a string, please try again!"

def test_service_create_session_issue_date_time_too_long():
    try:
        test_session = Session(0, -1, "this is too long and should bring about the desired error", str(session_expire))
        session_sao.service_create_session(test_session)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The issue date and time field cannot exceed 26 characters, please try again!"

def test_service_create_session_issue_date_time_empty():
    try:
        test_session = Session(0, -1, "", str(session_expire))
        session_sao.service_create_session(test_session)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The issue date and time field cannot be left empty, please try again!"

def test_service_create_session_expire_date_time_not_string():
    try:
        test_session = Session(0, -1, str(session_start), session_expire)
        session_sao.service_create_session(test_session)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The expire date and time field must be a string, please try again!"

def test_service_create_session_expire_date_time_too_long():
    try:
        test_session = Session(0, -1, str(session_start), "this is too long and should bring about the desired error")
        session_sao.service_create_session(test_session)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The expire date and time field cannot exceed 26 characters, please try again!"

def test_service_create_session_expire_date_time_empty():
    try:
        test_session = Session(0, -1, str(session_start), "")
        session_sao.service_create_session(test_session)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The expire date and time field cannot be left empty, please try again!"

def test_service_create_session_success():
    result = session_sao.service_create_session(successful_session)
    assert result.session_id != 0

def test_service_get_session_id_not_integer():
    try:
        session_sao.service_get_session("10")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The session ID field must be an integer, please try again!"

def test_service_get_session_not_found():
    try:
        session_sao.service_get_session(-500000000000)
        assert False
    except FailedTransaction as error:
        assert str(error) == "No session found, please try again!"

def test_service_get_session_expired():
    try:
        result = session_sao.service_get_session(-1)
        print(result)
        assert False
    except FailedTransaction as error:
        assert str(error) == "Session has expired, please log in!"

def test_service_get_session_success():
    result = session_sao.service_get_session(successful_session.session_id)
    assert result is not None

def test_service_delete_session_id_not_integer():
    try:
        session_sao.service_delete_session("1")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The session ID field must be an integer, please try again!"

def test_service_delete_session_not_found():
    try:
        session_sao.service_delete_session(-5000000000)
        assert False
    except FailedTransaction as error:
        assert str(error) == "No session found, please try again!"

def test_service_delete_session_success():
    result = session_sao.service_delete_session(successful_session.session_id)
    assert result
