from django.urls import path
from . import views

urlpatterns = [
    #page views
    #path('home', views.HomeView.as_view(), name='home'),
    path('about', views.AboutView.as_view(), name="about"),
    path('contact', views.contact, name="contact"),
    path('home', views.base.as_view(), name="base"),
    path('terms', views.terms_and_conditions, name="terms"),
    
    #list views
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('topics/', views.TopicListView.as_view(), name='topic-list'),
    
    #detail views
    #post detail view paths
    path('posts/<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.PostDetailView.as_view(),
         name='post-detail'),
    path(
        'posts/<int:pk>/',
        views.PostDetailView.as_view(),
        name='post-detail'),
    
    #topic detail view paths
    path('topics/<slug:slug>/',
         views.TopicDetailView.as_view(),
         name='topic-detail'),
    path('topics/<int:pk>',
         views.TopicDetailView.as_view(),
         name='topic-detail'),
        
]
