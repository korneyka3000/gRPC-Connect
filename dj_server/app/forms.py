from django import forms


class QuestionForm(forms.Form):
    body = forms.CharField(max_length=150, label='question')