from django import forms
from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# User Registration Form
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label = "Email",required=True)

    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    def save(self,commit=True):
        user = super(RegistrationForm,self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

# Create Whiteboard Form
class WhiteboardForm(UserCreationForm):
    subject = forms.CharField(label='Subject', max_length=30)
    # If checked, the whiteboard is open to the public
    public = forms.BooleanField(initial=True)
    if public == True:
        privatekey = forms.IntegerField(label='WhiteboardPassword')
