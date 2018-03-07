from django import forms


class userinput(forms.Form):
    q = forms.IntegerField(required=True,min_value=1, max_value=10000, label='Enter N',
        error_messages={'min_value': 'Minimum 1' , 'max_value': 'Maximum is set to 10000' })