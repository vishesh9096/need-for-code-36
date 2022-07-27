"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("homepage/",views.listTask,name='task_list'),
    path("loc",views.loc,name='loc'),
    path("signin",views.signin,name='signin'),
    path("signup",views.signup,name='signup'),
    path("aboutus",views.aboutus,name='aboutus'),
    path("contact",views.contact,name='contact'),
    path("contact",views.contact,name='contact'),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('delete_task/<str:pk>/', views.deleteTask, name="delete_task"),
	path('home/', views.listTask, name="task_list"),
	path('activity', views.activity, name="activity"),
	path('query', views.query, name="query"),

    
]
