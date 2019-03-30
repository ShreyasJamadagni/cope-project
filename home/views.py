from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'home/index.html', {'title': "Home"})

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            e = "\n" + "Sent by : " + form.cleaned_data['email']
            send_mail(
                "Query from website",
                form.cleaned_data['message'] + "\n" + e,
                form.cleaned_data['email'],
                [settings.EMAIL_HOST_USER],
                fail_silently=False
            )
            form.save()
            return redirect('page-home')

    return render(request, 'home/contact.html',{'title': 'Contact Us', 'form': form})
