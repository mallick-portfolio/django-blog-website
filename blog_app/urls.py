from django.urls import path
from .views import home, blogs, blogDetails, categoryblogs, tagBlogs

urlpatterns = [
    path("", home, name='home'),
    path("blogs/", blogs, name='blogs'),
    path("blogs/<int:pk>/", blogDetails, name='blog-details'),
    path("category/<str:slug>/", categoryblogs, name='category-blog'),
    path("tag/<str:slug>/", tagBlogs, name='tag-blog'),
]
