from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Article, UnreviewedArticle
from .forms import articleSubmitForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def viewArticles(request):
    # packet = {'articles1': Article.objects.all(), 'title': "Published Articles"}
    return render(request, 'articles/index.html', {'title': 'Published Articles', 'articles1': Article.objects.all()})

@login_required
def createArticle(request):
    form = articleSubmitForm()
    if request.method == 'POST':
        form = articleSubmitForm(request.POST)
        if form.is_valid():
            # form.cleaned_data['author'] = request.user
            v = form.save(commit=False)
            v.author = request.user
            v.save()
            messages.success(request, f'Article has been submitted for review')
            return redirect('view-articles')

    return render(request, 'articles/createArticle.html', {'title': "Publish an Article", 'form': form})

@login_required
def review(request):
    articles = UnreviewedArticle.objects.all()
    if request.method == 'GET':
        print('GET REQUEST!!!')
        title = request.GET.get('title')
        if title != None:
            article = UnreviewedArticle.objects.get(title=title)

            return render(request, 'articles/review.html', {'title': 'Review Submitted Articles', 'article': article})

    if request.method == "POST":
        title = request.POST.get('title')
        article = UnreviewedArticle.objects.get(title=title)
        accept = request.POST.get('accept')
        reject = request.POST.get('reject')

        if accept == "R":
            h = Article.objects.create(title=article.title, content=article.content, author=article.author)
            article.delete()

            send_mail(
                'Your article on COPE has been approved!',
                'Article has been approved',
                settings.EMAIL_HOST_USER,
                ['fineman3301@gmail.com'],
                fail_silently=False
            )

            messages.info(request, f'Article has been apporved and uploaded')
            return redirect('review')

        if reject == "R":
            send_mail(
                'Your article on COPE has been rejected',
                'Article has been rejected',
                settings.EMAIL_HOST_USER,
                [request.user.email],
                fail_silently=False
            )
            article.delete()

            messages.info(request, 'Article has been rejected')
            return redirect('review')

    print("unowww" + request.user.email + "YEEEEHAWW")
    return render(request, 'articles/review.html', {'title': 'Review Submitted Articles', 'articles': articles})
