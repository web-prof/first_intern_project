from django import forms
from django.core import validators


class screen2_form(forms.Form):
    country_choices = (
        ('', 'select country'),
        ('country1', 'country1'),
        ('country2', 'country2'),
        ('country1,2', 'country1,2'),
    )
    phone_code = (
        ('02', '02'),
        ('03', '03'),
    )
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "name": "first_name",
        "id": "first_name",
        "type": "text",
        "onfocus": "this.placeholder = ''",
        "onblur": "this.placeholder = 'first name'",
        "placeholder": 'first name',
        'pattern': '[A-Za-z]{0,}'

    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "name": "last_name",
        "id": "last_name",
        "type": "text",
        "onfocus": "this.placeholder = ''",
        "onblur": "this.placeholder = 'last name'",
        "placeholder": 'last name',
        'pattern': '[A-Za-z]{0,}'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "name": "email",
        "id": "email",
        "type": "text",
        "onfocus": "this.placeholder = ''",
        "onblur": "this.placeholder = 'work email address'",
        "placeholder": 'work email address',
    }))
    code = forms.CharField(widget=forms.Select(choices=phone_code, attrs={
        'class': 'form-control w-100',
        'id': 'phone_code',
        'name': 'phone_code',
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "name": "phone_number",
        "id": "phone_number",
        "type": "text",
        "onfocus": "this.placeholder = ''",
        "onblur": "this.placeholder = 'phone number'",
        "placeholder": 'phone number',
        "pattern": "[0-9]{0,}",
    }))
    operation_country = forms.CharField(widget=forms.Select(choices=country_choices, attrs={
        "class": "form-control w-100 mb-5",
        'placeholder': 'select country',
        'name':'operation_country',
        'id':'operation_country',

    }))
    company_name = forms.CharField(widget=forms.Select(attrs={
        "class": "form-control w-100 mb-5",
        'placeholder': 'select company',
        'name':'company_name',
        'id':'company_name',

    }))
    objective = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "name": "objective",
        "id": "objective",
        "type": "text",
        "onfocus": "this.placeholder = ''",
        "onblur": "this.placeholder = 'objective'",
        "placeholder": 'objective'

    }))
    more_details = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "name": "more_details",
        "id": "more_details",
        "type": "textarea",
        "onfocus": "this.placeholder = ''",
        "onblur": "this.placeholder = 'more details...'",
        "placeholder": 'more details...'
    }))

    class Select(forms.Select):
        def create_option(self, *args, **kwargs):
            option = super().create_option(*args, **kwargs)
            if not option.get('value'):
                option['attrs']['disabled'] = 'disabled'

            if option.get('value') == 2:
                option['attrs']['disabled'] = 'disabled'

            return option
