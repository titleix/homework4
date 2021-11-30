from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('update/<str:pk>/', views.update, name="update"),
    path('delete/<str:pk>/', views.delete, name="delete"),
    path('crossoff/<str:pk>', views.crossoff_item,name="crossoff_item"),
    path('uncross/<str:pk>', views.uncross_item,name="uncross_item"),
]