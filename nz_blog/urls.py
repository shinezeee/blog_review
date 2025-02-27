"""
URL configuration for nz_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('post/', include('post.urls'))
"""

from django.contrib import admin
from django.urls import include, path

import post
from post.views import post_delete, post_detail, post_edit, post_list, post_new

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("post.urls")),  # post url 포함시키기
]
