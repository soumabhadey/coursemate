from django.forms import ModelForm
from django import forms
from users.models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ["user", "interests"]

        labels = {
            "is_creator": "Are you a course creator or instructor? (This feature allows you to create blogs and announcements related to your course)"
        }

        widgets = {
            'image': forms.FileInput(),
            'displayname': forms.TextInput(attrs={"placeholder": "Add display name"}),
            "info": forms.Textarea(attrs={"rows": 3, "placeholder": "Add information"}),
        }



class UserSettingsForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        