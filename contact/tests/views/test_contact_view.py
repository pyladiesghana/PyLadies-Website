# Django imports
from django.core import mail
from django.shortcuts import reverse
from django.test import TestCase

# Pyladies imports


class TestContactView(TestCase):
    """
        Test contact view
    """

    def setUp(self) -> None:
        """
        Initialize data to be used for testing.

        :return: None
        """
        self.url = reverse("contact:contact")

    def test_contact_page_status_code(self):
        response = self.client.get(path='/contact/')
        self.assertEquals(response.status_code, 200)

    def test_contact_view_url_by_name(self):
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(path=self.url)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_contact_view_with_empty_data(self):
        """
        Test POST method with empty data
        """
        response = self.client.post(path=self.url, data={})
        self.assertEqual(response.status_code, 200)

    def test_contact_view_with_invalid_data(self):
        invalid_form_data = {
            "subject": "We want to sponsor you",
            "sender_email": "ghana@pyladies.com",
            "message": ""
        }
        response = self.client.post(path=self.url, data=invalid_form_data)
        self.assertEqual(len(mail.outbox), 0)

    def test_contact_view_with_valid_data(self):
        valid_form_data = {
            "subject": "We want to sponsor you",
            "sender_email": "ghana@pyladies.com",
            "message": "We want to sponsor your meetups"
        }
        response = self.client.post(path=self.url, data=valid_form_data)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "We want to sponsor you")





