"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import django
from django.test import TestCase

# TODO: Configure your database in settings.py and sync before running tests.

class SimpleTest(TestCase):
    """Tests for the application views."""

    # Django requires an explicit setup() when running tests in PTVS
    @classmethod
    def setUpClass(cls):
        super(SimpleTest, cls).setUpClass()
        django.setup()

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

        from django.test import TestCase
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm

class RegisterFormTest(TestCase):
    def test_register_form_valid(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

class LoginFormTest(TestCase):
    def test_login_form_valid(self):
        form_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())