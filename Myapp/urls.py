from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

   
    path("courses/", views.courses, name="courses"),
    path("video/", views.video, name="video"),
    path("survey/", views.survey, name="survey"),
    path("learning-hub/", views.learning, name="learning"),
    path("concept-map/", views.concept_map, name="concept_map"),
    path("problem-to-solve/", views.problem_to_solve, name="problem_to_solve"),
    path("post-test/", views.post_test, name="post_test"),
    path("survey-two/", views.survey_two, name="survey_two"),
    path("content/<slug:slug>/", views.course_detail, name="content"),
    path('track_video_event/', views.track_video_event, name='track_video_event'),

]



