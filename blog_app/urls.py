from django.urls import path
from .views import home, blogs, blogDetails

urlpatterns = [
    path("", home, name='home'),
    path("blogs/", blogs, name='blogs'),
    path("blogs/<int:pk>/", blogDetails, name='blog-details'),
]
