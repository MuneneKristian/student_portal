from django.contrib import admin
from django.urls import path
from django.shortcuts import render

# Views for your HTML pages
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),         # http://127.0.0.1:8000/ → home.html
    path('about/', about, name="about"), # http://127.0.0.1:8000/about/ → about.html
]
