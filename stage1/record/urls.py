from django.urls import path

from .views import Home, Result, History

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('result/<int:pk>/', Result.as_view(), name='result'),
    path('history/', History.as_view())
]