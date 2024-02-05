from .models import *
from django import forms

class Message_form(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            "name",
            "email",
            "phone_no",
            "subject",
            "content"
        ]
