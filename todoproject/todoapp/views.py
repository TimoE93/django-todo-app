import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    output = ", ".join([todo.title for todo in todos])
    return HttpResponse(output)


def detail(request, todo_id):
    response = "Todo %s"
    return HttpResponse(response % todo_id)