from django.urls import path, include, re_path
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.login, name='login'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('home/', views.poll_index, name='home'),
    path('register/', views.register, name='register'),
    path('', include('polls.urls')),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'), 
]