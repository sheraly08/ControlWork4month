from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect
from tasks.models import Task
from tasks.forms import TaskForm

# Create your views here.


def tasks_list(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()

    return render(request, "tasks/list.html", {"tasks": tasks})

def detail_list(request: HttpRequest, id: int) -> HttpResponse:
    task = Task.objects.get(id=id)
    return render(request, "tasks/detail.html", {"task": task})


def task_create(request: HttpRequest) -> HttpResponse:
    form = TaskForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("tasks_list")
    return render(request, "tasks/create.html", {"form": form})


def task_edit(request: HttpRequest, id: int) -> HttpResponse:
    article = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, request.FILES or None, instance=article)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("detail_list", id=form.instance.id)

    return render(request, "tasks/edit.html", {"form": form})
