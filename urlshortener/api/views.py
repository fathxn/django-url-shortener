from django.shortcuts import render, redirect
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Link
from .serializers import LinkSerializer
from django.views import View
from django.conf import settings

# Create your views here.
class ShortenerListAPIView(ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class ShortenerCreateAPIView(CreateAPIView):
    serializer_class = LinkSerializer

class Redirector(View):
    def get(self,request,url_shortener,*args,**kwargs):
        url_shortener = settings.HOST_URL+'/'+self.kwargs['url_shortener']
        redirect_url = Link.objects.filter(shorturl=url_shortener).first().longurl
        return redirect(redirect_url)