# Django imports
from django import forms


class ContactForm(forms.Form):
    """ Form for processing and validating contact message """

    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
                           "class": "form-control", "id": "name",
                           "type": "text", "placeholder": "Your Subject *",
                           "required": "required",
                           "data - validation - required - message":
                              "Please enter your subject."
                           }))

    sender_email = forms.EmailField(widget=forms.EmailInput(attrs={
                           "class": "form-control", "id":"email",
                           "type": "email", "placeholder": "Your Email *",
                           "required": "required",
                           "data - validation - required - message":
                                       "Please enter your email address."
                             }))

    message = forms.CharField(widget=forms.Textarea(attrs={
                                      "class": "form-control", "id":"message",
                                      "placeholder": "Your Message *",
                                      "required": "required",
                                      "data - validation - required - message":
                                      "Please enter a message."
                                      }))
