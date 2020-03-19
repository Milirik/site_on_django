"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index_url'),
    path('projects', projects_list, name='projects_list_url'),
    path('articles', articles_list, name='articles_list_url'),
    path('contacts', Contacts.as_view(), name='contacts_url'),
    path('post_detail/<slug>', PostDetail.as_view(), name='post_detail_url')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
