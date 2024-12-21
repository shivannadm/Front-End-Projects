from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('upload/', views.upload_dataset, name='upload_dataset'),
    path('select/', views.select_dataset, name='select_dataset'),
]
