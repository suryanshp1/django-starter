from django.shortcuts import render
from django.shortcuts import redirect

def home_view(request):
    # return render(request, 'home.html', {})
    return redirect('messageboard')