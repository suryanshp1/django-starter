from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def messageboard_view(request):
    # return render(request, 'a_messageboard/index.html', {})
    return redirect('messageboard')
