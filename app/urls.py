"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^lists/$', views.lists, name='lists'),
    url(r'^lists/create/$', views.create_list, name='new_list'),
    url(r'^lists/edit/(\d+)/$', views.EditList, name='edit'),
    url(r'^lists/delete/(\d+)/$', views.DeleteList, name='delete'),
    url(r'^lists/view/(\d+)/$', views.ViewList, name='view'),
    url(r'^lists/(\d+)/create_task/$', views.create_task, name='new_task'),
    url(r'^task/mark_complete/(\d+)/$', views.mark_task_complete, name='mark_task_complete'),
    url(r'^task/mark_incomplete/(\d+)/$', views.mark_task_incomplete, name='mark_task_incomplete'),
    url(r'^lists/(\d+)/task/edit/(\d+)/$', views.EditTask, name='edit_task'),
    url(r'^task/delete/(\d+)/$', views.DeleteTask, name='delete_task'),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
