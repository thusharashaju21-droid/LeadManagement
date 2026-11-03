
from django.urls import path

from accounts.views import AdminRegisterView,UserRegisterView,ProfileView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [

    #admin registration
    path("register/admin/",AdminRegisterView.as_view()),

    #user registration
    path("register/user/",UserRegisterView.as_view()),

    #jwt token creation
    path("jwt/token/",TokenObtainPairView.as_view()),

    #jwt token refresh
    path("jwt/token/refresh/",TokenRefreshView.as_view()),

    #profile listing
    path("profile/",ProfileView.as_view()),
]