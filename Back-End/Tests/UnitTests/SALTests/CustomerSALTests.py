from DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from Entities.Customer import Customer
from Entities.FailedTransaction import FailedTransaction
from SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)

successful_customer = Customer(0, "first", "last", "password", "new@email.com", "11234567890",
                               "123 First Street, City, State, ZIP")
successful_confirmation = "password"

def test_service_create_customer_first_name_not_string():
    try:
        test_customer = Customer(0, 0, "last", "password", "test@email.com", "11234567890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer, successful_confirmation)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The first name field must be a string, please try again!"

def test_service_create_customer_first_name_too_long():
    try:
        test_customer = Customer(0, "this has too many characters and so it should raise the desired exception",
                                 "last", "password", "test@email.com", "11234567890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer, successful_confirmation)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The first name field cannot exceed 36 characters, please try again!"

def test_service_create_customer_first_name_empty():
    try:
        test_customer = Customer(0, "", "last", "password", "test@email.com", "11234567890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer, successful_confirmation)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The first name field cannot be left empty, please try again!"

def test_service_create_customer_last_name_not_string():
    try:
        test_customer = Customer(0, "first", 0, "password", "test@email.com", "11234567890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer, successful_confirmation)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The last name field must be a string, please try again!"

def test_service_create_customer_last_name_too_long():
    try:
        test_customer = Customer(0, "first", "this has too many characters and so it should raise the desired exception"
                                 , "password", "test@email.com", "11234567890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer, successful_confirmation)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The last name field cannot exceed 36 characters, please try again!"

def test_service_create_customer_last_name_empty():
    try:
        test_customer = Customer(0, "first", "", "password", "test@email.com", "11234567890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer, successful_confirmation)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The last name field cannot be left empty, please try again!"

def test_service_create_customer_password_not_string():
    try:
        test_customer = Customer(0, "first", "last", 0, "test@email.com", "11234567890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer, successful_confirmation)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The password field must be a string, please try again!"

def test_service_create_customer_password_empty():
    try:
        test_customer = Customer(0, "first", "last", "", "test@email.com", "11234567890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer, successful_confirmation)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The password field cannot be left  empty, please try again!"

def test_service_create_customer_password_too_long():
    try:
        test_customer = Customer(0, "first", "last", "this is much too long and so it should fail and get the "
                                 "desired error message", "test@email.com", "11234567890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer, successful_confirmation)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The password field cannot exceed 36 characters, please try again!"

def test_service_create_customer_confirmation_password_empty():
    try:
        test_customer = Customer(0, "first", "last", "password", "test@email.com", "11234567890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer, "")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The confirmation password field cannot be left empty, please try again!"

def test_service_create_customer_confirmation_password_too_long():
    try:
        test_customer = Customer(0, "first", "last", "pass", "test@email.com", "11234567890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer, "this is much too long and should raise the desired error")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The confirmation password field cannot exceed 36 characters, please try again!"

def test_service_create_customer_confirmation_password_not_string():
    try:
        test_customer = Customer(0, "first", "last", "test", "test@email.com", "11234567890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer, 6)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The confirmation password field must be a string, please try again!"

def test_service_create_customer_email_not_string():
    try:
        test_customer = Customer(0, "first", "last", "password", 0, "11234567890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer, successful_confirmation)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The email field must be a string, please try again!"

def test_service_create_customer_email_too_long():
    try:
        test_customer = Customer(0, "first", "last", "password",
                                 "this has too many characters and so it should raise the desired exception",
                                 "11234567890", "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer, successful_confirmation)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The email field cannot exceed 60 characters, please try again!"

def test_service_create_customer_email_empty():
    try:
        test_customer = Customer(0, "first", "last", "password", "", "11234567890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer, successful_confirmation)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The email field cannot be left empty, please try again!"

def test_service_create_customer_phone_number_not_string():
    try:
        test_customer = Customer(0, "first", "last", "password", "test@email.com", 0,
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer, successful_confirmation)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The phone number field must be a string, please try again!"

def test_service_create_customer_phone_number_too_long():
    try:
        test_customer = Customer(0, "first", "last", "password", "test@email.com",
                                 "this has too many characters and so it should raise the desired exception",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer, successful_confirmation)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The phone number field cannot exceed 12 characters, please try again!"

def test_service_create_customer_phone_number_empty():
    try:
        test_customer = Customer(0, "first", "last", "password", "test@email.com", "",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_create_customer(test_customer, successful_confirmation)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The phone number field cannot be left empty, please try again!"

def test_service_create_customer_address_not_string():
    try:
        test_customer = Customer(0, "first", "last", "password", "test@email.com", "11234567890",
                                 0)
        customer_sao.service_create_customer(test_customer, successful_confirmation)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The address field must be a string, please try again!"

def test_service_create_customer_address_too_long():
    try:
        test_customer = Customer(0, "first", "last", "password", "test@email.com", "11234567890",
                                 "this has too many characters and so it should raise the desired exception")
        customer_sao.service_create_customer(test_customer, successful_confirmation)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The address field cannot exceed 60 characters, please try again!"

def test_service_create_customer_address_empty():
    try:
        test_customer = Customer(0, "first", "last", "password", "test@email.com", "11234567890",
                                 "")
        customer_sao.service_create_customer(test_customer, successful_confirmation)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The address field cannot be left empty, please try again!"

def test_service_create_customer_confirmation_password_not_matching_password():
    try:
        failed_confirmation = "not going to work"
        customer_sao.service_create_customer(successful_customer, failed_confirmation)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The passwords do not match, please try again!"

def test_service_create_customer_success():
    result = customer_sao.service_create_customer(successful_customer, successful_confirmation)
    assert result.customer_id != 0

def test_service_create_customer_already_exists():
    try:
        test_customer = Customer(0, "first", "last", "password", "new@email.com", "11234567890",
                                 "123 S 1st St, Dallas, Texas, 78999")
        customer_sao.service_create_customer(test_customer, successful_confirmation)
        assert False
    except FailedTransaction as error:
        assert str(error) == "A customer already exists with this username, please log in!"

def test_service_get_customer_by_id_not_integer():
    try:
        customer_sao.service_get_customer_by_id("this won't work")
        assert False
    except FailedTransaction as error:
        assert str(error) == "CustomerRoutes ID field must be an integer, please try again!"

def test_service_get_customer_by_id_not_found():
    try:
        customer_sao.service_get_customer_by_id(-500000)
        assert False
    except FailedTransaction as error:
        assert str(error) == "This customer cannot be found, please try again!"

def test_service_get_customer_by_id_success():
    result = customer_sao.service_get_customer_by_id(successful_customer.customer_id)
    assert result is not None

def test_service_get_customer_by_email_not_a_string():
    try:
        customer_sao.service_get_customer_by_email(50)
        assert False
    except FailedTransaction as error:
        assert str(error) == "Email field must be a string, please try again!"

def test_service_get_customer_by_email_success():
    result = customer_sao.service_get_customer_by_email(successful_customer.email)
    assert result is not None

def test_service_login_email_not_string():
    try:
        customer_sao.service_login(0, successful_customer.password)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The email field must be a string, please try again!"

def test_service_login_email_empty():
    try:
        customer_sao.service_login("", successful_customer.password)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The email field cannot be left empty, please try again!"

def test_service_login_password_not_string():
    try:
        customer_sao.service_login(successful_customer.email, 0)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The password field must be a string, please try again!"

def test_service_login_password_empty():
    try:
        customer_sao.service_login(successful_customer.email, "")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The password field cannot be left empty, please try again!"

def test_service_login_email_or_password_incorrect():
    try:
        customer_sao.service_login("incorrect", "credentials")
        assert False
    except FailedTransaction as error:
        assert str(error) == "Either the email or password are incorrect, please try again!"

def test_service_login_success():
    result = customer_sao.service_login("test@email.com", "work")
    assert result is not None

def test_service_update_customer_first_name_not_string():
    try:
        test_customer = Customer(successful_customer.customer_id, 0, "last", "password", "test@email.com",
                                 "11234567890", "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer, successful_customer.customer_id)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The first name field must be a string, please try again!"

def test_service_update_customer_first_name_empty():
    try:
        test_customer = Customer(successful_customer.customer_id, "", "last", "password", "test@email.com",
                                 "11234567890", "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer, successful_customer.customer_id)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The first name field cannot be empty, please try again!"

def test_service_update_customer_first_name_too_long():
    try:
        test_customer = Customer(successful_customer.customer_id,
                                 "this has too many characters and so it should raise the desired exception", "last"
                                 , "password", "test@email.com", "11234567890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer, successful_customer.customer_id)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The first name field cannot exceed 36 characters, please try again!"

def test_service_update_customer_last_name_not_string():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", 0, "password", "test@email.com",
                                 "11234567890", "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer, successful_customer.customer_id)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The last name field must be a string, please try again!"

def test_service_update_customer_last_name_too_long():
    try:
        test_customer = Customer(successful_customer.customer_id, "first",
                                 "this has too many characters and so it should raise the desired exception"
                                 , "password", "test@email.com", "11234567890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer, successful_customer.customer_id)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The last name field cannot exceed 36 characters, please try again!"

def test_service_update_customer_last_name_empty():
    try:
        test_customer = Customer(successful_customer.customer_id, "first",
                                 ""
                                 , "password", "test@email.com", "11234567890",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer, successful_customer.customer_id)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The last name field cannot be empty, please try again!"


def test_service_update_customer_email_not_string():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", "last", "password", 0,
                                 "11234567890", "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer, successful_customer.customer_id)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The email field must be a string, please try again!"

def test_service_update_customer_email_empty():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", "last", "password",
                                 "",
                                 "11234567890", "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer, successful_customer.customer_id)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The email field cannot be empty, please try again!"

def test_service_update_customer_email_too_long():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", "last", "password",
                                 "this has too many characters so it should raise the desired exception",
                                 "11234567890", "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer, successful_customer.customer_id)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The email field cannot exceed 60 characters, please try again!"

def test_service_update_customer_phone_number_not_string():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", "last", "password",
                                 "test@email.com", 0, "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer, successful_customer.customer_id)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The phone number field must be a string, please try again!"

def test_service_update_customer_phone_number_empty():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", "last", "password",
                                 "test@email.com", "",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer, successful_customer.customer_id)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The phone number field cannot be empty, please try again!"

def test_service_update_customer_phone_number_too_long():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", "last", "password",
                                 "test@email.com", "this should raise the desired exception",
                                 "123 First Street, City, State, ZIP")
        customer_sao.service_update_customer(test_customer, successful_customer.customer_id)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The phone number field cannot exceed 12 characters, please try again!"

def test_service_update_customer_address_not_string():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", "last", "password",
                                 "test@email.com", "11234567890", 0)
        customer_sao.service_update_customer(test_customer, successful_customer.customer_id)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The address field must be a string, please try again!"

def test_service_update_customer_address_empty():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", "last", "password",
                                 "test@email.com", "11234567890", "")
        customer_sao.service_update_customer(test_customer, successful_customer.customer_id)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The address field cannot be empty, please try again!"

def test_service_update_customer_address_too_long():
    try:
        test_customer = Customer(successful_customer.customer_id, "first", "last", "password",
                                 "test@email.com", "11234567890",
                                 "this has too many characters and so it should bring about the desired exception")
        customer_sao.service_update_customer(test_customer, successful_customer.customer_id)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The address field cannot exceed 60 characters, please try again!"

def test_service_update_customer_no_info_changed():
    try:
        customer_sao.service_update_customer(successful_customer, successful_customer.customer_id)
        assert False
    except FailedTransaction as error:
        assert str(error) == "No information has changed!"

def test_service_update_customer_success():
    updated_customer = Customer(successful_customer.customer_id, "new", "names", "new", "new@email.com",
                                "11234207890", "420 First Avenue, City, State, ZIP")
    result = customer_sao.service_update_customer(updated_customer, successful_customer.customer_id)
    assert result.first_name == updated_customer.first_name and result.last_name == updated_customer.last_name \
           and result.email == updated_customer.email and result.phone_number == updated_customer.phone_number \
           and result.address == updated_customer.address

def test_service_change_password_customer_not_found():
    try:
        customer_sao.service_change_password(-5000000000, "new", "new")
        assert False
    except FailedTransaction as error:
        assert str(error) == "This customer cannot be found, please try again!"

def test_service_change_password_password_new_password_not_string():
    try:
        customer_sao.service_change_password(successful_customer.customer_id, -500000, "new")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The new password field must be a string, please try again!"

def test_service_change_password_password_new_password_empty():
    try:
        customer_sao.service_change_password(successful_customer.customer_id, "", "new")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The password field cannot be left empty, please try again!"

def test_service_change_password_password_new_password_too_long():
    try:
        customer_sao.service_change_password(successful_customer.customer_id, "this is too long and so it should "
                                                                              "raise the desired error message", "new")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The password field cannot exceed 36 characters, please try again!"

def test_service_change_password_confirmation_password_not_string():
    try:
        customer_sao.service_change_password(successful_customer.customer_id, "new", -5000000)
        assert False
    except FailedTransaction as error:
        assert str(error) == "The confirmation password field must be a string, please try again!"

def test_service_change_password_password_confirmation_password_empty():
    try:
        customer_sao.service_change_password(successful_customer.customer_id, "new", "")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The confirmation password cannot be left empty, please try again!"

def test_service_change_password_password_confirmation_password_too_long():
    try:
        customer_sao.service_change_password(successful_customer.customer_id, "new", "this is too long and so it "
                                                                                     "should raise the desired error "
                                                                                     "message")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The confirmation password field cannot exceed 36 characters, please try again!"

def test_service_change_password_customer_id_not_integer():
    try:
        customer_sao.service_change_password("this won't work", "new", "new")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The customer ID field must be an integer, please try again!"

def test_service_change_password_new_password_does_not_match_confirmation_password():
    try:
        customer_sao.service_change_password(successful_customer.customer_id, "new", "old")
        assert False
    except FailedTransaction as error:
        assert str(error) == "The passwords don't match, please try again!"

def test_service_change_password_nothing_changed():
    try:
        customer_sao.service_change_password(successful_customer.customer_id, "password",
                                             "password")
        assert False
    except FailedTransaction as error:
        assert str(error) == "Nothing has changed, please try again!"

def test_service_change_password_success():
    result = customer_sao.service_change_password(successful_customer.customer_id, "new", "new")
    assert result

def test_service_delete_customer_not_found():
    try:
        customer_sao.service_delete_customer(-500000)
        assert False
    except FailedTransaction as error:
        assert str(error) == "This customer cannot be found, please try again!"

def test_service_delete_customer_success():
    result = customer_sao.service_delete_customer(successful_customer.customer_id)
    assert result
