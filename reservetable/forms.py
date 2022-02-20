
from .models import usermessage
from django import forms

class userform(forms.ModelForm):
    class Meta():
        model = usermessage
        fields = "__all__"
