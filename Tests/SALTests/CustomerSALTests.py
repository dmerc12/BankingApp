from DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from Entities.Customer import Customer
from Entities.FailedTransaction import FailedTransaction
from SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)

successful_customer = Customer(0, "first", "last", "username", "password", "test@email.com", "123-456-7890",
                               "123 First Street, City, State, ZIP")

def test_service_create_customer_first_name_not_string():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_first_name_too_long():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_first_name_empty():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_last_name_not_string():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_last_name_too_long():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_last_name_empty():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_username_not_string():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_username_too_long():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_username_empty():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_password_not_string():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_password_too_long():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_password_empty():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_email_not_string():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_email_too_long():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_email_empty():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_email_incorrect_format():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_phone_number_not_string():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_phone_number_too_long():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_phone_number_empty():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_phone_number_incorrect_format():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_address_not_string():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_address_too_long():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_address_empty():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_address_incorrect_format():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_create_customer_success():
    pass

def test_service_get_customer_by_id_not_integer():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_get_customer_by_id_not_found():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_get_customer_by_id_success():
    pass

def test_service_login_username_not_string():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_login_username_too_long():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_login_username_empty():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_login_password_not_string():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_login_password_too_long():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_login_password_empty():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_login_username_or_password_incorrect():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_login_success():
    pass

def test_service_update_customer_first_name_not_string():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_first_name_too_long():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_first_name_empty():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_last_name_not_string():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_last_name_too_long():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_last_name_empty():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_username_not_string():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_username_too_long():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_username_empty():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_password_not_string():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_password_too_long():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_password_empty():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_email_not_string():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_email_too_long():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_email_empty():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_email_incorrect_format():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_phone_number_not_string():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_phone_number_too_long():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_phone_number_empty():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_phone_number_incorrect_format():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_address_not_string():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_address_too_long():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_address_empty():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_address_incorrect_format():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_update_customer_success():
    pass

def test_service_delete_customer_id_not_integer():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_delete_customer_not_found():
    try:
        pass
    except FailedTransaction as error:
        assert str(error) == ""

def test_service_delete_customer_success():
    pass
