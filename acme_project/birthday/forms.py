from django import forms

from .models import BirthdayForm


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = BirthdayForm
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
