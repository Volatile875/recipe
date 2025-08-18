"""
URL configuration for vege project.

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))    from myapp.views import lag, first, delete_recepie

"""
from django.contrib import admin
from django.urls import path
from myapp.views import lag, first
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import delete_recepie



urlpatterns = [
     # This handles the root path
    path('', lag, name='lag'),
    path('first/', first, name='first'),
    path('delete-recepie<int:id>/', delete_recepie , name='delete-recepie'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                    document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()