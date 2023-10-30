import os

from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    subject = forms.CharField(label='Assunto', max_length=100)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f'Nome: {name}\nE-mail: {email}\nAssunto: {subject}\nMensagem: {message}'

        send_mail(
            subject=subject,
            message=content,
            from_email=os.environ.get('EMAIL_HOST_USER'),
            recipient_list=[email],
            fail_silently=False,
        )
