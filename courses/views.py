from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from courses.models import Subject, Course, Platform
from courses.forms import CourseForm

def get_subject_names_json_view(request):
    subject_names = Subject.objects.values_list("name", flat=True)

    return JsonResponse(list(subject_names), safe=False)



def get_platform_names_json_view(request):
    platform_names = Platform.objects.values_list("name", flat=True)

    return JsonResponse(list(platform_names), safe=False)



def course_create_view(request):
    context = {}
    form = CourseForm()
    platforms = Platform.objects.all()
    subjects = Subject.objects.all()

    if request.method == "POST":
        form = CourseForm(request.POST)
        tags = request.POST.get("tags")
        subject_name = request.POST.get("subject_name")
        platform_name = request.POST.get("platform_name")

        if form.is_valid():
            course = form.save(commit=False)
            course.subject = Subject.objects.get(name=subject_name)
            course.platform = Platform.objects.get(name=platform_name)
            course.tags = [tag.strip() for tag in tags.split(",")]
            course.save()
            return redirect("home")
        else:
            messages.success(request, "Course added successfully")
        


    context["form"] = form
    context["subjects"] = subjects
    context["platforms"] = platforms
            


    return render(request, "courses/course_create.html", context)


def courses_view(request):
    context = {}

    courses = Course.objects.all()

    context["courses"] = courses

    return render(request, "courses/courses.html", context)
