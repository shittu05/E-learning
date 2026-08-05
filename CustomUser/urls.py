from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path('register/',views.register, name = 'register'),
    path('login/',views.login, name = 'login'),
    path('logout/',views.logout, name = 'logout'),
    path('export/', views.export_page, name='export_page'),
    path('export/survey-one/', views.export_survey_one, name='export_survey_one'),
    path('export/survey-two/', views.export_survey_two, name='export_survey_two'),
    path('export/video-one/', views.export_video_one, name='export_video_one'),
    path('export/video-two/', views.export_video_two, name='export_video_two'),
    path('export/video-three/', views.export_video_three, name='export_video_three'),
    path('export/video-four/', views.export_video_four, name='export_video_four'),
    path('export/post-test/', views.export_post_test, name='export_post_test'),
    path('export/all/', views.export_all_submissions, name='export_all_submissions'),
]





