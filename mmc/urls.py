from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="/"),
    path('grafici', views.grafici, name="grafici"),
    path('delete/<int:id>', views.delete, name="delete")
]