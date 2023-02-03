from django.urls import path, include, re_path
from . import views

app_name = 'polls'
urlpatterns = [
    path('home', views.poll_index, name='poll'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),    
]