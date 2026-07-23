from django.urls import path
from . import views

urlpatterns = [
    path('', views.inspiration_list, name='inspiration_list'),
    path('<int:pk>/', views.inspiration_detail, name='inspiration_detail'),
]
