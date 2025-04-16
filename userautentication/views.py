from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse
from .forms import RegistrationFrom, UserForm, UserProfileForm
from .models import Account, UserProfile
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# verification email

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

# Create your views here.


def get_register(request):
    if request.method == 'POST':
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split("@")[0]

            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                               username=username, password=password)

            user.phone_number = phone_number

            user.save()

            # User Activation
            """current_sit = get_current_site(request)
            mail_subject = "Please active your account"
            message = render_to_string('account/account_verification_email.html', {
                'user': user,
                'domain': current_sit,
                'uid': urlsafe_base64_encode(force_bytes(user.id)),
                'token': default_token_generator.make_token(user)
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request,
                             f"Thank you for registering with us, We have sent you a verification email to your email address. Please verify it")
            return redirect('account:login') """
            return redirect('userauthencation:login')
        else:
            messages.error(request, 'Something went wrong!')
            return redirect('userauthencation:register')
    else:
        form = RegistrationFrom()
    context = {
        'form': form
    }

    return render(request, 'auth/register.html', context)


def get_login(request):
    if request.user.is_authenticated:
        return redirect('userauthencation:dashboard')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = auth.authenticate(username=email, password=password)
            print(user)
            if user is not None:
                auth.login(request, user)
                # messages.success(request, 'You are now logged in.')
                return redirect('userauthencation:dashboard')
            else:
                messages.error(request, 'Invalid Login credentials')
                return redirect('userauthencation:login')
    return render(request, 'auth/login.html')

@login_required
def get_logout(request):
    logout(request)
    messages.info(request, 'You are now loggout.')
    return HttpResponseRedirect(reverse('userauthencation:login'))
def get_dashboard(request):
    return render(request, 'core/index.html')
