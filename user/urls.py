from django.urls import path

from user.views import CreateUserAPI, GetOrUpdateOrDeleteSingleUserAPI

app_name = "user"

urlpatterns = [
    path("", CreateUserAPI.as_view(), name="add-user"),
    path("<int:pk>/", GetOrUpdateOrDeleteSingleUserAPI.as_view(), name="get-update-user")
]