from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    # Group name. Max length set to 50 characters to be able to use it as a slug. 
    title = models.CharField(max_length=50)

    # Part of the URL of the group (/group/<slug>). 
    # Must be unique and should be indexed for faster search in db
    slug = models.SlugField(unique=True, db_index=True)

    # Description of the group (more detailed than a title).
    # Max length not limited, we rely on our admins' 
    # common sense to not make massive descriptions
    description = models.TextField()


class Post(models.Model):
    # Content of the post
    text = models.CharField(max_length=200)

    # Date of post publication, default = now
    pub_date = models.DateTimeField(
        verbose_name="date published", auto_now_add=True)
    
    # Author of the post. Must be a registered user
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author")
    
    # A group where post is posted. A post does not need to belong to a group
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="post_group", 
        blank=True, null=True)