from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import NewTopic
from .models import Topic

# Create your views here.
@login_required
def home(request):
    topics = Topic.objects.all()
    print(request.GET)
    return render(request, 'debate/home.html', {'title': 'Debate', 'topics': topics})

@login_required
def newTopic(request):
    form = NewTopic()

    if request.method == 'POST':
        form = NewTopic(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, f'Topic has been registered')
            return redirect('debate-home')

    return render(request, 'debate/newTopic.html', {'title': 'Create Topic', 'form': form})
