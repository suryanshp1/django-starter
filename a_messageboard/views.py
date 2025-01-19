from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import MessageBoard
from django.shortcuts import get_object_or_404
from .forms import MessageCreateForm
from django.contrib import messages
from .utils import send_email

# Create your views here.

@csrf_exempt
@login_required
def messageboard_view(request):
    messageboard = get_object_or_404(MessageBoard, id=1)
    form = MessageCreateForm()

    if request.method == 'POST':
        if request.user in messageboard.subscribers.all():
            form = MessageCreateForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.author = request.user
                message.messageboard = messageboard
                message.save()
                send_email(message)

        else:
            messages.warning(request, 'You are not subscribed to this messageboard!')

        return redirect('messageboard')

    context = {'messageboard': messageboard, 'form': form}
    return render(request, 'a_messageboard/index.html', context)


@login_required
def subscribe(request):
    messageboard = get_object_or_404(MessageBoard, id=1)

    if request.user not in messageboard.subscribers.all():
        messageboard.subscribers.add(request.user)
        messageboard.save()

    else:
        messageboard.subscribers.remove(request.user)
        messageboard.save()

    return redirect('messageboard')