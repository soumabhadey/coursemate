from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from users.forms import ProfileForm, UserSettingsForm


def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            return redirect("account_login")
    context = {}
    context["profile"] = profile
    return render(request, "users/profile.html", context)


def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)
    interests = ", ".join(request.user.profile.interests or [])
    context = {}

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        interests = request.POST.get("interests")
        if form.is_valid():
            profile = form.save(commit=False)

            profile.interests = [interest.strip() for interest in request.POST.get("interests").split(",")]
            profile.save()
            return redirect("profile")
        
    if request.path == reverse("profile_onboarding"):
        onboarding = True
    else:
        onboarding = False
    
    context["form"] = form
    context["interests"] = interests
    context["onboarding"] = onboarding
    return render(request, "users/profile_edit.html", context)




@login_required(login_url="account_login")
def avatar_delete_view(request):
    context = {}

    profile = request.user.profile

    if request.method == "POST":
        profile = request.user.profile
        profile.image.delete()
        messages.success(request, "Avatar deleted successfully")
        return redirect("profile_edit")

    return render(request, "users/avatar_delete.html", context)



@login_required(login_url="account_login")
def user_view(request):
    context = {}
    context["user"] = request.user
    return render(request, "users/user.html", context)




@login_required(login_url="account_login")
def user_settings_view(request):
    context = {}
    user = request.user
    form = UserSettingsForm(instance=user)

    if request.method == "POST":
        form = UserSettingsForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, "Your account information was updated successfully.")
            return redirect('user')
        

    context["form"] = form

    return render(request, "users/user_settings.html", context)




@login_required(login_url="account_login")
def user_password_change_view(request):
    context = {}
    user = request.user
    form = PasswordChangeForm(user)

    if request.method == "POST":
        form = PasswordChangeForm(user, request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Prevent user from being logged out
            messages.success(request, "Your password was updated successfully.")
            return redirect('user')
        else:
            messages.error(request, "Invalid old password or weak new password")
        

    context["form"] = form

    return render(request, "users/user_password_change.html", context)



@login_required(login_url="account_login")
def user_delete_view(request):
    context = {}

    user = request.user

    if request.method == "POST":
        user = request.user
        user.delete()
        messages.success(request, "Account deleted successfully")
        return redirect("home")
    
    return render(request, "users/user_delete.html", context)
