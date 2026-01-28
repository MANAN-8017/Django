# polls/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('calc/', views.calc, name='calc'),
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]