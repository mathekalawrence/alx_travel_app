from django.urls import path
from . import views

urlpatterns = [
    # The actual endpoints to be added later
    path('', views.listings_home, name='listings-home'),
]