from django.urls import path,include
from app import views
urlpatterns= [
    path('',views.home),
    path('trend/',views.search),
    path('trend/<str:trend>/',views.trend),
]