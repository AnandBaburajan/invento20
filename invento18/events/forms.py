from django import forms
from .models import Event_register, Event

class EventRegisterForm(forms.ModelForm):

    class Meta:
            model = Event_register
            fields = [
                'first_name',
                'last_name',
                'email',
                'phone',
                'referal_code'
            ]

class AmbassadorForm(forms.Form):

    first_name = forms.CharField(label='first_name',max_length=50)
    last_name = forms.CharField(label='lastname',max_length=50)
    email =  forms.EmailField(label='email',max_length=254)
    phone = forms.CharField(label='phone',max_length=20)
    college = forms.CharField(label='college',max_length=250)
    department = forms.CharField(label='department',max_length=250)

class Loginform(forms.Form):

    email = forms.EmailField(label='email',max_length=254)
    referal_code = forms.IntegerField(label='referal_code')
