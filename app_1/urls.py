from django.contrib import admin
from django.urls import path
from app_1 import views

urlpatterns = [
    path('', views.home),
    path('news/', views.veiw_new),
]

handler404 = 'app_1.views.Page404Html'