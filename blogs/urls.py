from django.urls import path

from blogs.views import blogs_view, blog_view, blogs_my_view, blogs_search_view

urlpatterns = [
    path("", blogs_view, name="blogs"),
    path("blogs_my/", blogs_my_view, name="blogs_my"),
    path("blogs_search/", blogs_search_view, name="blogs_search"),
    path("<id>/", blog_view, name="blog")
]