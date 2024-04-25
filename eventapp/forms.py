from django import forms
from . models import Registration
class DateInput(forms.DateInput):
    input_type='date'

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Registration
        fields='__all__'

        # widgets={
        #     'event_date':DateInput(),
        # }


        labels={
            'reg_name':"Attendee Name",
            'reg_email':"Attendee Email",
            'name':"Event",
        }