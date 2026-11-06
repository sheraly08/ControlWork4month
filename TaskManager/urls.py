"""
URL configuration for TaskManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks.views import tasks_list, detail_list, task_create, task_edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", tasks_list, name="tasks_list"),
    path("task/<int:id>/", detail_list, name="detail_list"),
    path("create/", task_create, name="task_create"),
    path("<int:id>/edit/", task_edit, name="task_edit"),
]
