from django.urls import path

from .views import (
    api_detailall_page_view
)

app_name = 'auth'

urlpatterns = [
    path("",api_detailall_page_view,name="page_detailall")
]