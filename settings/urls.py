"""
URL configuration for acm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.template import RequestContext
from django.urls import path, include

def index(request):
    return render(request=request, template_name="home.html")

def handler404(request, *args, **argv):
    return render(request,'404.html')

urls = [
    path('', index, name="index"),
    path('',include('apps.groups.urls')),
    path('questions',include('apps.questinos.urls')),
]

if settings.NEED_ADMIN:
    urls.append(path('admin/', admin.site.urls))

urls.append(path('404/',handler404))

urlpatterns =  urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)