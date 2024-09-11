import re
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Todo
from .forms import TodoForm

def index(request):
    todos = Todo.objects.all()
    output = ", ".join([todo.title for todo in todos])
    context = {
        "todos": todos
    }

    return render(request, "todoapp/index.html", context)


def detail(request, todo_id):
    import pdb; pdb.set_trace()
    todo = get_object_or_404(Todo, pk=todo_id)
    form = TodoForm(instance=todo)
    
    
    return render(request, "todoapp/detail.html", {"todo": todo, "form": form})