from django.urls import path
from . import views

# Empty path means home page.
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
]
