from django.db import models
from accounts.models import User
from django.utils.text import slugify


# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, default=title)
    created_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, default=title)
    created_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class Blog(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_blogs')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category_blogs')
    tags = models.ManyToManyField(Tag, blank=True, related_name='tag_blogs')
    title = models.CharField(max_length=250, unique=True)
    slug = models.CharField(max_length=250, default=title)

    banner = models.ImageField(upload_to='blog_banners')
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_comments',
        on_delete=models.CASCADE
    )
    blog = models.ForeignKey(
        Blog,
        related_name='blog_comments',
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text


class Reply(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_replies',
        on_delete=models.CASCADE
    )
    comment = models.ForeignKey(
        Comment,
        related_name='comment_replies',
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text