from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UnregisteredUser
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.html import format_html

# Create your views here.
def register(request):
    found = False
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        for m in User.objects.all():
            for t in UnregisteredUser.objects.all():
                if m.email == request.POST.get('email') or t.email == request.POST.get('email'):
                    found = True

        if found == False:
            if form.is_valid():
                v = form.save(commit=False)
                n = UnregisteredUser.objects.create(username=v.username, email=v.email, password=v.password, registration_code=str(hash(v.email)))
                n.save()

                send_mail(
                    'COPE registration confirmation',
                    'Code: ' + n.registration_code,
                    settings.EMAIL_HOST_USER,
                    [n.email],
                    fail_silently=False
                )

                return redirect('confirm')

        if found == True:
            messages.info(request, 'A user with that email already exists. Please try to login or confirm your registration')
            return redirect('register')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Register New User'})

@login_required
def profile(request):
    return render(request, 'users/profile.html', {'title': "Profile of " + request.user.username})

@login_required
def changePassword(request):
    form = PasswordChangeForm(request.user)

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')

    return render(request, 'users/changePassword.html', {'title': "Change Passowrd", 'form': form})

def confirmRegistration(request):
    # registered = False
    if request.method == 'POST':
        registration_code = request.POST.get('regCode')

        for n in UnregisteredUser.objects.all():
            if registration_code == n.registration_code:
                registered_user = User.objects.create(username=n.username, email=n.email, password=n.password)
                instance = UnregisteredUser.objects.get(id=n.id)
                instance.delete()
                # registerd = True
                messages.success(request, f'You have been registered to COPE')
                return redirect('login')

        # if registered == False:
        messages.info(request, f'Registration Code cannot be validated. Please ren-enter your code')
        return redirect('login')

    return render(request, 'users/confirmation.html', {'title': 'Registration Confirmation'})
