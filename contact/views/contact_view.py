# Django imports
from django.core.mail import BadHeaderError, send_mail
from django.contrib import messages
from django.shortcuts import render, redirect

# Contact app imports
from contact.forms.contact_form import Contact
from contact.utils import PYLADIES_EMAIL


def contact(request):

    # if this is a POST request we process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request
        contact_form = Contact(request.POST)

        # check whether the form data is valid else display error message
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            sender_email = contact_form.cleaned_data['sender_email']
            message = contact_form.cleaned_data['message']

            # Email recipients
            recipients = [PYLADIES_EMAIL, ]

            # check if the fields are not empty
            if subject and sender_email and message:

                # process the data in form.cleaned_data as required
                try:
                    send_mail(subject, message, sender_email, recipients,
                              fail_silently=False)
                except BadHeaderError:
                    messages.error(recipients, "Invalid header found.")
                else:
                    # Alert success message and redirect user to a new URL
                    messages.success(request,
                                     "Your message was sent successfully. "
                                     "We will get back to you "
                                     "as soon as possible through your email !")
                    return redirect('contact:contact')
            else:
                messages.error(request, "Please no field should be left blank !")

        else:
            messages.error(request, "Please provide valid information !!")

    # if the request is GET (or any other method) create a blank form
    else:
        contact_form = Contact()

    context = {'contact_form': contact_form}
    template_name = 'contact/contact.html'

    return render(request, template_name, context)
