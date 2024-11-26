import markdown
from django.shortcuts import render, redirect
from django.db.models import Q
from blogs.models import Blog

def blogs_view(request):
    context = {}
    blogs = Blog.objects.all().order_by("-date_created")
    context["blogs"] = blogs
    return render(request, "blogs/blogs.html", context)



def blogs_my_view(request):
    context = {}
    blogs = Blog.objects.filter(author=request.user.profile).order_by("-date_created")
    context["blogs"] = blogs
    return render(request, "blogs/blogs.html", context)



def blogs_search_view(request):
    context = {}
    if request.method == "POST":
        query = request.POST.get("search_query")
        blogs = Blog.objects.filter(Q(title__icontains=query) | Q(body__icontains=query)).order_by("-date_created")
        context["blogs"] = blogs
        return render(request, "blogs/blogs.html", context)
    else:
        return redirect("blogs")





def blog_view(request, id):
    context = {}
    id = int(id)
    blog = Blog.objects.get(id=id)
    blog.body_html = markdown.markdown(blog.body)
    context["blog"] = blog
    return render(request, "blogs/blog.html", context)



def blog_create_view(request):
    context = {}
    return render(request, "blogs")

