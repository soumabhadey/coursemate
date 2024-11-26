from django.db import models
from users.models import Profile



class Subject(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self) -> str:
		return self.name
      

class Platform(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self) -> str:
		return self.name



class Course(models.Model):
    title = models.CharField(max_length=100)
    about = models.TextField(null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    uploader = models.CharField(max_length=20)
    instructor = models.CharField(max_length=50, null=True, blank=True)
    url = models.URLField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(Profile, related_name="liked_courses", blank=True)
    tags = models.JSONField(null=True, blank=True)

    @property
    def like_count(self):
          return self.likes.count()

    def __str__(self):
        return str(self.title)
