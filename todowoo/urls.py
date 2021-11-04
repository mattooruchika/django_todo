"""todowoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from todo import views as t_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTH
    path('signup/', t_views.signup_user,name='signup_user'),
    path('login/', t_views.login_user,name='login_user'),
    path('logout/', t_views.logout_user,name='logout_user'),

    # TODOVALS
    path('', t_views.home,name='home'),
    path('create/', t_views.createtodos,name='createtodos'),
    path('current/', t_views.currenttodos,name='currenttodos'),
    path('completed/', t_views.completedtodos,name='completedtodos'),
    path('todo/<int:todo_pk>', t_views.viewtodo,name='viewtodo'),
    path('todo/<int:todo_pk>/complete', t_views.completetodo,name='completetodo'),
    path('todo/<int:todo_pk>/delete', t_views.deletetodo,name='deletetodo'),
]
