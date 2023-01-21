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
        test_customer = Customer(0, 0, "last", "username", "password", "test@email.com", "123-456-7890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The first name field must be a string, please try again!"

def test_service_create_customer_first_name_too_long():
    try:
        test_customer = Customer(0, "this has too many characters and so it should raise the desired exception",
                                 "last", "username", "password", "test@email.com", "123-456-7890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The first name field cannot exceed 36 characters, please try again!"

def test_service_create_customer_first_name_empty():
    try:
        test_customer = Customer(0, "", "last", "username", "password", "test@email.com", "123-456-7890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The first name field cannot be left empty, please try again!"

def test_service_create_customer_last_name_not_string():
    try:
        test_customer = Customer(0, "first", 0, "username", "password", "test@email.com", "123-456-7890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The last name field must be a string, please try again!"

def test_service_create_customer_last_name_too_long():
    try:
        test_customer = Customer(0, "first", "this has too many characters and so it should raise the desired exception"
                                 , "username", "password", "test@email.com", "123-456-7890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The last name field cannot exceed 36 characters, please try again!"

def test_service_create_customer_last_name_empty():
    try:
        test_customer = Customer(0, "first", "", "username", "password", "test@email.com", "123-456-7890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The last name field cannot be left empty, please try again!"

def test_service_create_customer_username_not_string():
    try:
        test_customer = Customer(0, "first", "last", 0, "password", "test@email.com", "123-456-7890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The username field must be a string, please try again!"

def test_service_create_customer_username_too_long():
    try:
        test_customer = Customer(0, "first", "last",
                                 "this has too many characters and so it should raise the desired exception",
                                 "password", "test@email.com", "123-456-7890", "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The username field cannot exceed 36 characters, please try again!"

def test_service_create_customer_username_empty():
    try:
        test_customer = Customer(0, "first", "last", "", "password", "test@email.com", "123-456-7890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The username field cannot be left empty, please try again!"

def test_service_create_customer_password_not_string():
    try:
        test_customer = Customer(0, "first", "last", "username", 0, "test@email.com", "123-456-7890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The password field must be a string, please try again!"

def test_service_create_customer_password_too_long():
    try:
        test_customer = Customer(0, "first", "last", "username",
                                 "this has too many characters and so it should raise the desired exception",
                                 "test@email.com", "123-456-7890", "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The password field cannot exceed 36 characters, please try again!"

def test_service_create_customer_password_empty():
    try:
        test_customer = Customer(0, "first", "last", "username", "", "test@email.com", "123-456-7890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The password field cannot be left  empty, please try again!"

def test_service_create_customer_email_not_string():
    try:
        test_customer = Customer(0, "first", "last", "username", "password", 0, "123-456-7890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The email field must be a string, please try again!"

def test_service_create_customer_email_too_long():
    try:
        test_customer = Customer(0, "first", "last", "username", "password",
                                 "this has too many characters and so it should raise the desired exception",
                                 "123-456-7890", "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The email field cannot exceed 36 characters, please try again!"

def test_service_create_customer_email_empty():
    try:
        test_customer = Customer(0, "first", "last", "username", "password", "", "123-456-7890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The email field cannot be left empty, please try again!"

def test_service_create_customer_phone_number_not_string():
    try:
        test_customer = Customer(0, "first", "last", "username", "password", "test@email.com", 0,
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The phone number field must be a string, please try again!"

def test_service_create_customer_phone_number_too_long():
    try:
        test_customer = Customer(0, "first", "last", "username", "password", "test@email.com",
                                 "this has too many characters and so it should raise the desired exception",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The phone number field cannot exceed 13 characters, please try again!"

def test_service_create_customer_phone_number_empty():
    try:
        test_customer = Customer(0, "first", "last", "username", "password", "test@email.com", "",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The phone number field cannot be left empty, please try again!"

def test_service_create_customer_phone_number_incorrect_format():
    try:
        test_customer = Customer(0, "first", "last", "username", "password", "test@email.com", "1234567890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The phone number must follow the format xxx-xxx-xxxx, please try again!"

def test_service_create_customer_address_not_string():
    try:
        test_customer = Customer(0, "first", "last", "username", "password", "test@email.com", "123-456-7890",
                                 0)
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The address field must be a string, please try again!"

def test_service_create_customer_address_too_long():
    try:
        test_customer = Customer(0, "first", "last", "username", "password", "test@email.com", "123-456-7890",
                                 "this has too many characters and so it should raise the desired exception")
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The address field cannot exceed 50 characters, please try again!"

def test_service_create_customer_address_empty():
    try:
        test_customer = Customer(0, "first", "last", "username", "password", "test@email.com", "123-456-7890",
                                 "")
        customer_sao.service_create_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The address field cannot be left empty, please try again!"

def test_service_create_customer_success():
    result = customer_sao.service_create_customer(successful_customer)
    assert result.customer_id != 0

def test_service_get_customer_by_id_not_integer():
    try:
        customer_sao.service_get_customer_by_id("this won't work")
        assert False
    except FailedTransaction as error:
        assert str(error) == "Customer ID field must be an integer, please try again!"

def test_service_get_customer_by_id_not_found():
    try:
        customer_sao.service_get_customer_by_id(-500000)
        assert False
    except FailedTransaction as error:
        assert str(error) == "This customer cannot be found, please try again!"

def test_service_get_customer_by_id_success():
    result = customer_sao.service_get_customer_by_id(successful_customer.customer_id)
    assert result is not None

def test_service_login_username_not_string():
    try:
        customer_sao.service_login(0, successful_customer.password)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The username field must be a string, please try again!"

def test_service_login_username_empty():
    try:
        customer_sao.service_login("", successful_customer.password)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The username field cannot be left empty, please try again!"

def test_service_login_username_too_long():
    try:
        customer_sao.service_login("this is too long so it should raise the desired exception",
                                   successful_customer.password)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The username field cannot exceed 36 characters, please try again!"

def test_service_login_password_not_string():
    try:
        customer_sao.service_login(successful_customer.username, 0)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The password field must be a string, please try again!"

def test_service_login_password_empty():
    try:
        customer_sao.service_login(successful_customer.username, "")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The password field cannot be left empty, please try again!"

def test_service_login_password_too_long():
    try:
        customer_sao.service_login(successful_customer.username, "this is too long so it should raise the desired "
                                                                 "exception")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The password field cannot exceed 36 characters, please try again!"


def test_service_login_username_or_password_incorrect():
    try:
        customer_sao.service_login("incorrect", "credentials")
        assert False
    except FailedTransaction as error:
        assert str(error) == "Either the username or password are incorrect, please try again!"

def test_service_login_success():
    result = customer_sao.service_login(successful_customer.username, successful_customer.password)
    assert result is not None

def test_service_update_customer_first_name_not_string():
    try:
        test_customer = Customer(successful_customer.customer_id, 0, "last", "username", "password", "test@email.com",
                                 "123-456-7890", "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The first name field must be a string, please try again!"

def test_service_update_customer_first_name_too_long():
    try:
        test_customer = Customer(successful_customer.customer_id,
                                 "this has too many characters and so it should raise the desired exception", "last"
                                 , "username", "password", "test@email.com", "123-456-7890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The first name field cannot exceed 36 characters, please try again!"

def test_service_update_customer_last_name_not_string():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", 0, "username", "password", "test@email.com",
                                 "123-456-7890", "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The last name field must be a string, please try again!"

def test_service_update_customer_last_name_too_long():
    try:
        test_customer = Customer(successful_customer.customer_id, "first",
                                 "this has too many characters and so it should raise the desired exception"
                                 , "username", "password", "test@email.com", "123-456-7890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The last name field cannot exceed 36 characters, please try again!"

def test_service_update_customer_username_not_string():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", "last", 0, "password", "test@email.com",
                                 "123-456-7890", "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The username field must be a string, please try again!"

def test_service_update_customer_username_too_long():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", "last",
                                 "this has too many characters and so it should raise the desired exception",
                                 "password", "test@email.com", "123-456-7890", "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The username field cannot exceed 36 characters, please try again!"

def test_service_update_customer_password_not_string():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", "last", "username", 0, "test@email.com",
                                 "123-456-7890", "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The password field must be a string, please try again!"

def test_service_update_customer_password_too_long():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", "last", "username",
                                 "this has too many characters and so it should raise the desired exception",
                                 "test@email.com", "123-456-7890", "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The password field cannot exceed 36 characters, please try again!"

def test_service_update_customer_email_not_string():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", "last", "username", "password", 0,
                                 "123-456-7890", "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The email field must be a string, please try again!"

def test_service_update_customer_email_too_long():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", "last", "username", "password",
                                 "this has too many characters so it should raise the desired exception",
                                 "123-456-7890", "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The email field cannot exceed 36 characters, please try again!"

def test_service_update_customer_phone_number_not_string():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", "last", "username", "password",
                                 "test@email.com", 0, "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The phone number field must be a string, please try again!"

def test_service_update_customer_phone_number_too_long():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", "last", "username", "password",
                                 "test@email.com", "this should raise the desired exception",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The phone number field cannot exceed 13 characters, please try again!"

def test_service_update_customer_phone_number_incorrect_format():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", "last", "username", "password",
                                 "test@email.com", "1234567890", "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The phone number must follow the format xxx-xxx-xxxx, please try again!"

def test_service_update_customer_address_not_string():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", "last", "username", "password",
                                 "test@email.com", "123-456-7890", 0)
        customer_sao.service_update_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The address field must be a string, please try again!"

def test_service_update_customer_address_too_long():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", "last", "username", "password",
                                 "test@email.com", "123-456-7890",
                                 "this has too many characters and so it should bring about the desired exception")
        customer_sao.service_update_customer(test_customer)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The address field cannot exceed 50 characters, please try again!"

def test_service_update_customer_success():
    updated_customer = Customer(successful_customer.customer_id, "new", "names", "new", "new", "new@email.com",
                                "123-420-7890", "420 First Avenue, City, State, ZIP")
    result = customer_sao.service_update_customer(updated_customer)
    assert result.first_name == updated_customer.first_name and result.last_name == updated_customer.last_name \
           and result.username == updated_customer.username and result.password == updated_customer.password \
           and result.email == updated_customer.email and result.phone_number == updated_customer.phone_number \
           and result.address == updated_customer.address

def test_service_delete_customer_not_found():
    try:
        customer_sao.service_delete_customer(-500000)
        assert False
    except FailedTransaction as error:
        assert str(error) == "This customer cannot be found, please try again!"

def test_service_delete_customer_success():
    result = customer_sao.service_delete_customer(successful_customer.customer_id)
    assert result
