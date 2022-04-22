from django.urls import path
from . import views

# quite literally needs to be called urlpatterns. with an s. seriously
urlpatterns = [
    path('', views.get_data),
    path('add/', views.add_item),
]