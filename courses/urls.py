from django.urls import path
from courses.views import get_subject_names_json_view, get_platform_names_json_view, course_create_view, courses_view

# from blogs.views import blogs_view, blog_view, blogs_my_view, blogs_search_view

# urlpatterns = [
#     path("", blogs_view, name="blogs"),
#     path("blogs_my/", blogs_my_view, name="blogs_my"),
#     path("blogs_search/", blogs_search_view, name="blogs_search"),
#     path("<id>/", blog_view, name="blog")
# ]



urlpatterns = [
    path("get_subject_names_json/", get_subject_names_json_view, name="get_subject_names_json"),
    path("get_platform_names_json/", get_platform_names_json_view, name="get_platform_names_json"),
    path("course_create/", course_create_view, name="course_create"),

    path("", courses_view, name="courses")
]