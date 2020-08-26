from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    Choices = [('librarian','Librarian'),('student','Student')]
    designation = forms.RadioSelect(choices=Choices)

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('designation',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.designation = self.cleaned_data['designation']
        if commit:
            user.save()
        return user