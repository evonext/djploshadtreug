from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('triangle_area_calculator/', views.triangle_area_calculator, name='triangle_area_calculator'),

]
