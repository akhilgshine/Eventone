from django.forms import ModelForm
from django import forms
from events.models import *
from django.utils.translation import ugettext_lazy as _

from django.forms.fields import *
from django.forms.widgets import *


# class RegisterForm(forms.Form):

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    error_messages = {
        'invalid_login': _('The username credential is unknown.'),
        'invalid_pass': _('Invalid password or PIN'),
        'inactive': _('This account is inactive'),
    }

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'


class EventRegisterForm(forms.Form):
    table = forms.CharField(widget=forms.HiddenInput(), initial=123)
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=255, required=True)
    payment = forms.CharField(max_length=255, required=True)
    amount_paid = forms.FloatField(required=True)

    # payment = ChoiceField(label='',
    # 	initial='bank',
    # 	widget=RadioSelect(renderer=TabRadioRenderer),
    # 	choices=(('cash','Cash'),('paytm','PayTm'),('credit/debit','Credit/Debit')))


class HotelForm(forms.ModelForm):
    checkin_date = forms.CharField(required=True)
    checkout_date = forms.CharField(required=True)

    class Meta:
        model = Hotels
        fields = ('room_type', 'hotel_name', 'tottal_rent')

    def __init__(self, *args, **kwargs):
        super(HotelForm, self).__init__(*args, **kwargs)
        self.fields['room_type'].widget.attrs['class'] = 'form-control'
        self.fields['hotel_name'].widget.attrs['placeholder'] = 'Hotel Name'
        self.fields['hotel_name'].widget.attrs['class'] = 'form-control'
        self.fields['hotel_name'].widget.attrs['readonly'] = 'readonly'

        self.fields['tottal_rent'].widget.attrs['class'] = 'form-control'
        self.fields['tottal_rent'].widget.attrs['placeholder'] = 'Rent'
        self.fields['tottal_rent'].widget.attrs['readonly'] = 'readonly'

        self.fields['checkin_date'].widget.attrs['class'] = 'datepicker form-control'
        self.fields['checkout_date'].widget.attrs['class'] = 'datepicker form-control'


class UpdatePaymentForm(forms.ModelForm):
    class Meta:
        model = RegisteredUsers
        fields = ('amount_paid',)

    def __init__(self, *args, **kwargs):
        super(UpdatePaymentForm, self).__init__(*args, **kwargs)
        self.fields['amount_paid'].widget.attrs['class'] = 'form-control'


class UpgradeStatusForm(forms.ModelForm):
    amount_to_upgrade = forms.IntegerField(required=True)

    class Meta:
        model = RegisteredUsers
        fields = ('amount_paid', 'event_status')

    def __init__(self, *args, **kwargs):
        super(UpgradeStatusForm, self).__init__(*args, **kwargs)
        self.fields['amount_paid'].widget.attrs['class'] = 'form-control'
        self.fields['event_status'].widget.attrs['class'] = 'form-control'
        self.fields['amount_to_upgrade'].widget.attrs['class'] = 'form-control'
        self.fields['amount_to_upgrade'].widget.attrs['readonly'] = 'readonly'
