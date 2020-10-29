from django.urls import path
from . import views

# Empty path means home page.
urlpatterns = [
    path('', views.me, name='me-home'),
]