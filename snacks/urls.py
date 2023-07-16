from django.urls import path
from .views import HomeView,SnackListView,DetailView

urlpatterns = [
    path('',SnackListView.as_view(),name="snacks"),
    path('<int:pk>/',DetailView.as_view(),name="details")
]