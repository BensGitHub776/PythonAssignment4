
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from blog.models import Post, Topic, Comment
from django.shortcuts import render
from django.db.models import Count, CharField, Value
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from . import models



#simple views for the contact, and terms and conditions page
def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def terms_and_conditions(request):
    template = loader.get_template('tac.html')
    return HttpResponse(template.render())

#test view
class base(TemplateView):
    template_name = ('blog/base.html')
    def get_context_data(self, **kwargs):
        # Get the parent context
        context = super().get_context_data(**kwargs)
        latest_posts = Post.objects.filter(status="Published") \
            .order_by('-published')[:3]

        context.update({'latest_posts': latest_posts})

        return context

class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        # Get the parent context
        context = super().get_context_data(**kwargs)
        latest_posts = Post.objects.filter(status="Published") \
            .order_by('-published')[:3]

        context.update({'latest_posts': latest_posts})

        return context


#Class based view for the about page 
class AboutView(TemplateView):
    def get(self, request):


        comments = Comment.objects.all().values()
        template = loader.get_template('about.html')
        context = {
            
            "Comments": comments
        }

        return HttpResponse(template.render(context, request))

    def post(self,request):
        #post method, to be used in future
        print("POST")


#code for list/detail views

class PostListView(ListView):
    """
    Post model's list view
    """
    model = Post
    context_object_name = 'posts'

class PostDetailView(DetailView):
    """
    Post model's detail view
    """
    model = Post

class TopicListView(ListView):
    """
    Topic model's list view
    """
    model = Topic
    context_object_name = 'topics'

class TopicDetailView(DetailView):
    """
    Topi model's detail view
    """
    model = Topic
    # override context data
    def get_context_data(self, *args, **kwargs):
        #stores the topics slug in a var
        slug = (self.kwargs['slug'])
        topics = Topic.objects.all()
        topic = topics.filter(slug=self.kwargs['slug']).values('name').first()
        print(topic)
        topic_posts = (Post.objects.filter(topic__slug=slug))
   
        context = {
            "topic_posts": topic_posts,
            "topic_count": topic_posts.count,
            "topic": topic
                
            }

        return context