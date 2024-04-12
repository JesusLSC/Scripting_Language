from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='blog-home'), ### localhost:8000/  <---> blog-home
	path('about/', views.about, name='blog-about'), ### localhost:8000/about <----> blog-about
	
]