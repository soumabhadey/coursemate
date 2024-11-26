from django.contrib import admin
from courses.models import Subject, Platform, Course

admin.site.register(Subject)
admin.site.register(Platform)
admin.site.register(Course)