from django.urls import path, include
from django.contrib import admin
from salary_prediction import views

# salary_prediction/urls.py

from django.urls import path
from . import views
# salary_prediction/urls.py
urlpatterns = [
    # This line ensures the view function 'predict_view' is used.
    path('', views.predict_view, name='predict'),
]
