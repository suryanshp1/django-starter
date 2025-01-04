from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import ProfileForm, EmailForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from allauth.account.utils import send_email_confirmation
from django.contrib import messages

# Create your views here.


def profile_view(request, username = None):
    if username:
        profile = get_object_or_404(User, user__username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            return redirect('account_login')
    return render(request, 'a_users/profile.html', {"profile": request.user.profile})

@login_required
def profile_edit_view(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return render(request, 'a_users/profile.html', {"profile": request.user.profile})

    if request.path == reverse('profile-onboarding'):
        onboarding = True
    else:
        onboarding = False

    form = ProfileForm(instance=request.user.profile)
    return render(request, 'a_users/profile_edit.html', { "form": form, "onboarding": onboarding })

@login_required
def profile_settings_view(request):
    return render(request, 'a_users/profile_settings.html', {})

@login_required
def profile_emailchange_view(request):
    if request.htmx:
        form = EmailForm(instance=request.user)
        return render(request, 'partials/email_form.html', {"form": form})

    if request.method == 'POST':
        form = EmailForm(request.POST, instance=request.user)
        if form.is_valid():
            if User.objects.filter(email=form.cleaned_data['email']).exclude(id=request.user.id).exists():
                messages.warning(request, 'Email already in use')
                return redirect('profile_settings')
            form.save()

            # Then send updates emailaddress and set verified to false

            send_email_confirmation(request, request.user)

            return redirect('profile_settings')
        else:
            messages.warning(request, 'Form is not valid.')
    
    return redirect('home')

@login_required
def profile_emailverify_view(request):
    send_email_confirmation(request, request.user)
    return redirect('profile_settings')

@login_required
def profile_delete_view(request):
    user = request.user
    if request.method == 'POST':
        logout(request)
        user.delete()
        messages.success(request, 'User deleted')
        return redirect('home')
    return render(request, 'a_users/profile_delete.html', {})