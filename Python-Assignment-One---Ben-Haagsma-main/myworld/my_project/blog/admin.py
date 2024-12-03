'''used to register models to the admin'''
from django.contrib import admin
from . import models

#comment inline class
#used to display a post's comments when viewing it
#in the detailed view
class CommentInLine(admin.TabularInline):
    '''Used to add a posts comments to its display view'''
    model = models.Comment


#the admin classes are used to customize the list and search fields for each model
class PostAdmin(admin.ModelAdmin):
    '''used to customize how the list displays and search function for the post model'''
    list_display = (
        'title',
        'updated',
        'created',
        #sets it so, title and the updated/created timestamps are displayed
        #in the admin
    )

    list_filter = (
        'status',
        'topic',
    )
    #gives the option to filer by status and topic for posts

    #sets the slug field to be prepopulated with the title of the blog post
    prepopulated_fields = {'slug':('title',)}

    search_fields = (
        'title',
        'author__username'
    )
    #allows the user to search for posts by title, author username

    inlines = [
        CommentInLine,
    ]


class TopicAdmin(admin.ModelAdmin):
    '''used to customize how the list displays and search function for the topic model'''
    list_display = (
        'name',
        'slug',
    )
    #displays topics by name

    #sets the slug field to be prepopulated with the name of the topic
    prepopulated_fields = {'slug':('name',)}

    #allows user to search for topics by name
    search_fields = (
        'name',
    )

class CommentAdmin(admin.ModelAdmin):
    '''used to customize how the list displays and search function for the comment model'''
    list_display = (
        'name',
        'created',
        'updated',
    )
    #displays name, and the created/updated fields
    #for the comment model, in the admin

    search_fields = (
        'name',
    )
    #allows user to search for comments
    #by the name of the commenter

# Registers the models, and their corresponding admin classes
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.Comment, CommentAdmin)
