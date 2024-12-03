from django.contrib.auth import get_user_model
from django.db.models import Sum, Q, Max, Count

from blog.models import Comment, Post

User = get_user_model()



def question_1_return_active_users():
    """
    Return the results of a query which returns a list of all
    active users in the database.
    """
    User.objects.fiter(is_active=True)

def question_2_return_regular_users():
    """
    Return the results of a query which returns a list of users that
    are *not* staff and *not* superusers
    """
    User.objects.fiter(is_superuser=False,is_staff=False)

def question_3_return_all_posts_for_user(user):
    """
    Return all the Posts authored by the user provided. Posts should
    be returned in reverse chronological order from when they
    were created.
    """
    Post.objects.filter(author__username=user).order_by('-created')


def question_4_return_all_posts_ordered_by_title():
    """
    Return all Post objects, ordered by their title.
    """
    Post.objects.all().order_by('title')


def question_5_return_all_post_comments(post):
    """
    Return all the comments made for the post provided in order
    of last created.
    """
    Comment.objects.filter(post=post).order_by("-created")



def question_6_return_the_post_with_the_most_comments():
    """
    Return the Post object containing the most comments in
    the database. Do not concern yourself with approval status;
    return the object which has generated the most activity.
    """
    posts = Post.objects.annotate(total_comments=Count('comments'))

    posts.order_by('total_comments').values('title', 'total_comments')


def question_7_create_a_comment(post):
    """
    Create and return a comment for the post object provided.
    """
    comment = Comment()
    repr(comment)
    post_og = Post.objects.get(post)
    comment.post = post_og 
    comment.save()

def question_8_set_approved_to_false(comment):
    """
    Update the comment record provided and set approved=False
    """
    comment.approved = False
    comment.save()

def question_9_delete_post_and_all_related_comments(post):
    """
    Delete the post object provided, and all related comments.
    """
    post.delete()