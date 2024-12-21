from django.urls import path
from . import views

urlpatterns = [
    
    path('upload/', views.upload_dataset, name='upload_dataset'),
    path('select/', views.select_dataset, name='select_dataset'),
    path('predict/<int:dataset_id>/', views.predict_stock, name='predict_stock'),
]
