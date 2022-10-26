from django.urls import path
from articles import views


urlpatterns = [
    path('index/', views.Index.as_view(), name='index'),
]