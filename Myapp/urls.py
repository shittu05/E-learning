from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

   
    path("courses/", views.courses, name="courses"),
    path("content/<slug:slug>/", views.course_detail, name="content"),
  

]



