'''Module containing the models for the blog app'''
from django.conf import settings
from django.db import models
from django.urls import reverse

#blog models, includes Post, topics, and comments model


class Topic(models.Model):
    """
    Model representing a blog topic
    """
    name = models.CharField(unique=True, null=False, max_length=255)
    #name of the topic, cant be null
    slug = models.SlugField(max_length=255, null=False)
    #slug field for the topic, gets prepopulated with the topic name

    def __str__(self):
        return str(self.name)
    #override for topics str method, returns the topic name
    
    #returns topic absolute url, used in the topic detail views
    def get_absolute_url(self):
        if self.status == "PUBLISHED": 
            kwargs={
                "name": self.name,
                'slug': self.slug
                }
        else:
                kwargs = {'pk': self.pk}
        return reverse('post-detail', kwargs=kwargs)
    
    #custom method i added to shorten some code
    #returns all posts that have a given topic

        


class PostManager(models.Manager):
    def published(self):
        return self.filter(status=self.model.PUBLISHED)

    def drafts(self):
        return self.filter(status=self.model.DRAFT)

class Post(models.Model):
    """
    Model representing a blog post
    """
    title = models.CharField(max_length=255, null=False)
    #title property, non-nullable

    content = models.TextField(null=True)
    #content property, nullable

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='blog_posts',
        null=True
    )
    #author foreign key

    topic = models.ManyToManyField(
        Topic,
        related_name='topics',
        null=True
    )
    #topic foreign fey

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #created/updated properties
    #created is the timestamp for when the post is created
    #updated is the timestamp for when the post was last updated


    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The date/time the article was published'
    )
    #published property
    #timestamp for when the post switches from draft to published

    DRAFT = 'draft'
    PUBLISHED = 'published'
    status_choices = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]
    status = models.CharField(
        max_length=10,
        choices=status_choices,
        default=DRAFT,
        help_text='Set to published to make this publicly visible'
    )
    #status property, says if the post is a draft or published

    slug = models.SlugField(max_length=255, null=False)
    #slug field, prepopulates with the title field

    #returns post absolute url, used in the post detail views
    def get_absolute_url(self):
        if self.status == "PUBLISHED": 
            kwargs={
                "year": self.published.year,
                'month': self.published.month,
                'day': self.published.day,
                'slug': self.slug
                }
        else:
                kwargs = {'pk': self.pk}
        return reverse('post-detail', kwargs=kwargs)
    

    class Meta:
        '''used to set default list ordering for the post model'''
        ordering = ['-created']
        #used to set how the post list in the admin is sorted
        #currently sorts by created descending

    def __str__(self):
        return str(self.title)
        #override for the post str method, returns the posts title instead of the default text
    #objects = models.Manager
    #Post = PostManager()




class Comment(models.Model):
    """
    Model representing a blog comment
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.PROTECT,
        related_name='comments',
        null=False
    )
    #post foreign key
    #post in which the comment has been left on

    name = models.CharField(max_length=255, null=False)
    #username of the commenter

    email = models.CharField(max_length=255, null=False)
    #email of the commenter

    text = models.TextField(null=False)
    #text of the comment

    approved = models.BooleanField(default=False)
    #boolean field for if the comment has been approved

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #created/updated timestamps for the comment


    class Meta:
        '''used to set default list ordering for the comment model'''
        ordering = ['-created']

    def __str__(self):
        return str(self.name)
    #override for the comments str method, returns commenters name
    #might change this later???


