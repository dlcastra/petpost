import phonenumbers
from django import forms

from app.models import Order, LegalServices


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["email", "name", "phone", "description", "address_from", "address_to"]
        labels = {
            "name": "Imię",
            "phone": "Telefon",
            "description": "Opis",
            "address_from": "Adres wysyłki(pełny adres)",
            "address_to": "Adres dostawy(pełny adres)",
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        if len(email) > 255:
            raise forms.ValidationError("The e-mail address is too long")

        return email

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) > 50:
            raise forms.ValidationError("Name is too long, max length is 50")

        if any(char.isdigit() for char in name):
            raise forms.ValidationError("The name must not contain any numbers")

        return name

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if not phone:
            raise forms.ValidationError("Phone cannot be empty")

        if len(phone) < 9:
            raise forms.ValidationError("The number provided is too short")

        try:
            parsed = phonenumbers.parse(phone, None)
        except phonenumbers.NumberParseException as error:
            raise forms.ValidationError(f"{error.args[0]}")

        formatted_phone = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        return formatted_phone


class LegalServicesForm(forms.ModelForm):
    class Meta:
        model = LegalServices
        fields = ["email", "name", "phone", "description"]
        labels = {
            "name": "Imię",
            "phone": "Telefon",
            "description": "Opis",
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        if len(email) > 255:
            raise forms.ValidationError("The e-mail address is too long")

        return email

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) > 50:
            raise forms.ValidationError("Name is too long, max length is 50")

        if any(char.isdigit() for char in name):
            raise forms.ValidationError("The name must not contain any numbers")

        return name

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if not phone:
            raise forms.ValidationError("Phone cannot be empty")

        if len(phone) < 9:
            raise forms.ValidationError("The number provided is too short")

        try:
            parsed = phonenumbers.parse(phone, None)
        except phonenumbers.NumberParseException as error:
            raise forms.ValidationError(f"{error.args[0]}")

        formatted_phone = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        return formatted_phone
