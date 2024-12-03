from blog.models import Post, Topic, Comment

def base_context(request):
    """
    sends context vars to the blog views
    """
    posts = Post.objects.all() # returns the top 10 posts
    topics = Topic.objects.order_by("-name")
    topics= Topic.objects.all()
    #add authors query here


    topic_dict = {}
        #i was having a lot of trouble getting annotations working so i converted the topic data into a dict instead
    for t in topics:
        topic_dict[t.name] = (posts.filter(topic__name=t.name).count())
    return {
        "Topics": topic_dict,
        "Posts": posts,    
            }