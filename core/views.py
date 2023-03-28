from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import UserLoginForm , UserRegistrationForm 
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request ,"main.html")


def login_register(request):
    login_form = UserLoginForm()
    register_form = UserRegistrationForm()
    if request.method == 'POST':
        if 'login' in request.POST:
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home') # replace with the URL of your home page
        elif 'register' in request.POST:
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                return redirect('home') # replace with the URL of your home page
    return render(request, 'login.html', {'login_form': login_form, 'register_form': register_form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            recipients = [settings.EMAIL_HOST_USER]

            # Render email templates
            email_template = 'contact_email.html'
            context = {'subject': subject, 'message': message, 'sender': sender}
            html_message = render(request, email_template, context).content.decode('utf-8')

            # Send email
            send_mail(subject, message, sender, recipients, fail_silently=False, html_message=html_message)
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def story(request):
    return render(request, "story.html")

def services(request):
    return render(request, "servies/servies.html")

def services1(request):
    return render(request, "servies/services1.html")

def services2(request):
    return render(request, "servies/services2.html")

def services3(request):
    return render(request, "servies/services3.html")

def services4(request):
    return render(request, "servies/services4.html")

def services5(request):
    return render(request, "servies/services5.html")

def services6(request):
    return render(request, "servies/services6.html")