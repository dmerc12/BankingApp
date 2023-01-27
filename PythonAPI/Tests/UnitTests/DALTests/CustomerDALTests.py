from PythonAPI.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from PythonAPI.Entities.Customer import Customer

customer_dao = CustomerDALImplementation()
test_customer = Customer(0, "A test", "This is", "username", "password", "test@email.com", "123-456-7890",
                         "123 Test Street, City, State, ZIP")
updated_customer = Customer(test_customer.customer_id, "updated", "names", "new_username", "new_password",
                            "updated@email.com", "098-765-4321", "321 Updated Street, City, State, ZIP")

def test_create_customer_success():
    result = customer_dao.create_customer(test_customer)
    assert result.first_name == test_customer.first_name and result.last_name == test_customer.last_name and \
           result.username == test_customer.username and result.password == test_customer.password and \
           result.email == test_customer.email and result.phone_number == test_customer.phone_number and \
           result.address == test_customer.address

def test_get_customer_by_id_success():
    result = customer_dao.get_customer_by_id(test_customer.customer_id)
    assert result.customer_id == test_customer.customer_id

def test_get_customer_by_email_success():
    result = customer_dao.get_customer_by_email(test_customer.email)
    assert result is not None

def test_login_success():
    result = customer_dao.login("please", "work")
    assert result is not None

def test_update_customer_success():
    result = customer_dao.update_customer(updated_customer)
    assert result.first_name == updated_customer.first_name and result.last_name == updated_customer.last_name and \
           result.username == updated_customer.username and result.password == updated_customer.password and \
           result.email == updated_customer.email and result.phone_number == updated_customer.phone_number and \
           result.address == updated_customer.address

def test_delete_customer_success():
    result = customer_dao.delete_customer(test_customer.customer_id)
    assert result
