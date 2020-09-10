from django.urls import path
from django.views.generic import ListView, DetailView
from . import views
from django.contrib.auth import views as auth_views
from .models import News

urlpatterns = [
    # path('', views.home, name='home'),
    path('', ListView.as_view(queryset=News.objects.all().order_by("-pub_date")[:10], template_name="blog/home.html"), name='home'),
    path('<int:news_id>/', views.detail, name='detail'),
    path('<int:news_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('register', views.register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

]
