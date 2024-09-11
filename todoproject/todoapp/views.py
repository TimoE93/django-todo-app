import re
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from .models import Todo
from .forms import TodoForm


def index(request):
    todos = Todo.objects.all()
    output = ", ".join([todo.title for todo in todos])
    context = {
        "todos": todos
    }

    return render(request, "todoapp/index.html", context)


class Detail(View):
    form_class = TodoForm
    template_name = "todoapp/detail.html"

    def get(self, request, todo_id):
        todo = get_object_or_404(Todo, pk=todo_id)
        form = self.form_class(instance=todo)
        return render(request, self.template_name, {"todo": todo, "form": form})

    
    def post(self, request, todo_id):
        todo = get_object_or_404(Todo, pk=todo_id)
        form = self.form_class(request.POST, instance=todo)

        form.save()

        return JsonResponse({"state": "success"})
       # return redirect(reverse('todoapp:index'))



class DetailCreate(View):
    form_class = TodoForm
    template_name = "todoapp/detail_create.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    
    def post(self, request):
        form = self.form_class(request.POST)

        form.save()

        return redirect(reverse('todoapp:index'))