from django.urls import path
from . import views

app_name = "todoapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:todo_id>/", views.Detail.as_view(), name="detail")
]
