from django.urls import path
from . import views

app_name = "todoapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("todo/<int:todo_id>/", views.Detail.as_view(), name="detail"),
    path("createtodo/", views.DetailCreate.as_view(), name="detail_create")
]
