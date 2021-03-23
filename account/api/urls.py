from django.urls import path
from account.api.views import (
    api_registerAccount_view,
)

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
    path('register/', api_registerAccount_view, name="register"),
    path('login/', obtain_auth_token, name="login")
]
