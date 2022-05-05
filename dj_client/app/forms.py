from django import forms

from app.models import Jobs


class MyForm(forms.Form):
    title = forms.CharField(max_length=30, label='Job name')


class AddForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = [
            'title',
            'level',
            'salary',
            'location',
        ]

