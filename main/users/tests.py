from django.test import TestCase
from .models import *

# Tests for user model
class TestUserModel(TestCase):

    # Setup before tests
    def setUp(self):
        self.base_user = User.objects.create(first_name='first', last_name='last', username='firstlast', password='testuser', email='testuser@example.com')
        self.user = CustomUser.objects.create(phone_number='1-234-567-8901', user=self.base_user)

    # Test string method
    def test_string_method(self):
        user_str = str(self.user)
        expected_str = f'{self.user.user.first_name} {self.user.user.last_name}'
        self.assertEqual(user_str, expected_str)

    # Test first_name method
    def test_first_name_method(self):
        first_name = self.user.first_name()
        self.assertEqual(first_name, self.user.user.first_name)

    # Test last_name method
    def test_last_name_method(self):
        last_name = self.user.last_name()
        self.assertEqual(last_name, self.user.user.last_name)

    # Test email method
    def test_email_method(self):
        email = self.user.email()
        self.assertEqual(email, self.user.user.email)

    # Test username method
    def test_username_method(self):
        username = self.user.username()
        self.assertEqual(username, self.user.user.username)
