from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.


def profile_view(request):
    return render(request, 'a_users/profile.html', {"profile": request.user.profile})

@login_required
def profile_edit_view(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return render(request, 'a_users/profile.html', {"profile": request.user.profile})

    form = ProfileForm(instance=request.user.profile)
    return render(request, 'a_users/profile_edit.html', { "form": form })

