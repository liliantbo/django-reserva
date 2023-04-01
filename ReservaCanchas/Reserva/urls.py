from django.urls import path
from . import views

urlpatterns = [
    path('getInfoCanchaById/<int:id_cancha>', views.getInfoCanchaById, name='getInfoCanchaById'),
]
