from django.urls import path
from api.views import ShortenerCreateAPIView, ShortenerListAPIView

urlpatterns = [
    path('', ShortenerListAPIView.as_view(), name='get-url'),
    path('create/', ShortenerCreateAPIView.as_view(), name='create-shorten-url'),
]