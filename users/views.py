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

# Create your views here.

def register(request):
    current_user = request.user
    found = False
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            for m in User.objects.all():
                for t in UnregisteredUser.objects.all():
                    if m.email == form.cleaned_data['email'] or t.email == form.cleaned_data['email']:
                        found = True

            if found == False:
                form.save()

                send_mail(
                    'Registration confirmation at COPE',
                    'CODE: ' + str(hash(form.cleaned_data['email'])),
                    settings.EMAIL_HOST_USER,
                    [form.cleaned_data['email']],
                    fail_silently=False,
                )

                messages.success(request, f'An Email has been sent. Please refer to the email to confirm your registration')
                return redirect('confirm')
            elif found == True:
                messages.info(request, f'A user with this email exists. Please try to login through the login page.')
                return redirect('login')
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
    if type(request.user) == "User":
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

        return render(request, 'users/confirmation.html', {'title': 'Registration Confirmation'})
    else:
        messages.info(request, f'You were logged in as a user and cannot confirm another account. You have now been logged out and now can confirm your other accounts')
        return redirect('logout')
