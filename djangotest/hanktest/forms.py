from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='用戶id')
    password = forms.CharField(label='用戶密碼', widget=forms.PasswordInput())
