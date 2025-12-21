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
    path('export/problem-to-solve/', views.export_problem_to_solve, name='export_problem_to_solve'),
    path('export/post-test/', views.export_post_test, name='export_post_test'),
    path('export/all/', views.export_all_submissions, name='export_all_submissions'),
]





