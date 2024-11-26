from django.db import models
from django.templatetags.static import static
from users.models import Profile
from courses.models import Course

class Blog(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to="blog_images/", null=True, blank=True)
    tags = models.JSONField(null=True, blank=True)
    body = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    

    @property
    def banner(self):
        try:
            banner = self.image.url
        except:
            banner = static("images/avatar.svg")

        return banner
