from django.conf.urls import url
from users_app import views


app_name = "users_app"

urlpatterns = [
	url(r"^register/$", views.register, name="register")
	
]