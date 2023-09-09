from django.urls import path
from .views import WordRetrieveView

urlpatterns = [
    path('add/', WordRetrieveView.as_view(), name="add_word"),
    path('<int:pk>/', WordRetrieveView.as_view(), name="retrieve_word"),
]