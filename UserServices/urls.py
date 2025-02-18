from django.urls import path
from UserServices.Controller import AuthController

urlpatterns = [
    path("login/", AuthController.LoginAPIView.as_view(), name="login"),
]
