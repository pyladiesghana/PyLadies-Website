# Django imports
from django.test import TestCase

# Contact App imports.
from contact.forms.contact_form import ContactForm


class TestContactForm(TestCase):
    """
       Test contact form with valid and invalid data.
    """

    def setUp(self) -> None:
        """
        Sets up dummy data to be used by all test cases.

        :return: None
        """

        self.valid_form_data = {
            "subject": "We want to sponsor you",
            "sender_email": "ghana@pyladies.com",
            "message": "We want to sponsor your meetups"
        }

        self.invalid_form_data = {
            "subject": "We want to sponsor you",
            "sender_email": "ghana@pyladies.com",
            "message": ""
        }

        self.invalid_email_data = {
            "subject": "We want to sponsor you",
            "sender_email": "ghana.com",
            "message": "We want to sponsor your meetups"
        }

        self.empty_fields = {
            "subject": "",
            "sender_email": "",
            "message": ""
        }

    def test_contact_form_with_valid_data(self):
        contact_form = ContactForm(data=self.valid_form_data)
        self.assertTrue(contact_form.is_valid())
        self.assertFalse(contact_form.errors)

    def test_contact_form_with_invalid_data(self):
        contact_form = ContactForm(data=self.invalid_form_data)
        self.assertFalse(contact_form.is_valid())
        self.assertTrue(contact_form.errors)

    def test_contact_form_with_invalid_email(self):
        contact_form = ContactForm(data=self.invalid_email_data)
        self.assertEqual(contact_form.errors, {
            'sender_email': ['Enter a valid email address.']
        })

    def test_contact_form_with_empty_fields(self):
        contact_form = ContactForm(data=self.empty_fields)
        self.assertFalse(contact_form.is_valid())
        self.assertEqual(contact_form.errors, {
            'subject': ['This field is required.'],
            'sender_email': ['This field is required.'],
            'message': ['This field is required.']
        })
