from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=30)
    # phone_no = forms.CharField(max_length = 20)
    # first_name = forms.CharField(max_length = 20)
    # last_name = forms.CharField(max_length = 20)
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', "password1", "password2"]

    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")