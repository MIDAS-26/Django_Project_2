from django import forms
from django.contrib.auth.models import User
from users_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=froms.PasswordInput())

	class Meta():
		model = user
		fields = ("username", "email", "password")


class UserProfileInfoForm():
	class Meta():
		fields = ("portfolio_site", "profile_pic")


