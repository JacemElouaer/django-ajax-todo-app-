from django.urls import path
from .views import *

urlpatterns = [
    path('', apiOverview, name="overview"),
    path('', apiOverview, name="overview")
]
