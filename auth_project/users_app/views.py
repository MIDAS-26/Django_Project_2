from django.shortcuts import render

# Create your views here.


def index(request):
	return render(request, "users_app/index.html")

def register(request):
	registered = False
	
	if request.method == "POST":
		user_form = UserForm(data=request.POST)