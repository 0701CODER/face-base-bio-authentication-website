"""face_recognition_2_factor_auth URL Configuration

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
from xml.dom.minidom import Document
from django.conf import settings
from django.conf.urls.static import static

from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from face_auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('django_two_factor_face_auth.urls'))
    path('',views.home,name='home'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/',views.login_user,name='login'),
    path('facecam_feed/<str:user>/', views.facecam_feed, name='facecam_feed'),
    path('welcome/<str:user>',views.welcome,name='welcome'),
    path('checkAuth/<str:user>',views.checkAuth,name='check'),
    path('logout/',views.logout_user,name='logout'),
    path('face_auth',include('face_auth.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
