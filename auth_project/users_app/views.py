from django.shortcuts import render
from django.contrib.auth.models import User
from users_app.models import UserProfileInfo

# Create your views here.


def index(request):
	return render(request, "users_app/index.html")

def register(request):
	registered = False
	
	if request.method == "POST":
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileInfoForm(data=request.POST)