from django import forms
from .models import FitnessModel


class NewUserForm(forms.ModelForm):
    class Meta:
        model = FitnessModel
        exclude = ['userTableForeignKey']
