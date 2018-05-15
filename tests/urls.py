from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('test/<int:test_id>/', get_test_by_id),
    path('submit_test/<int:test_id>/', submit_test)
]
