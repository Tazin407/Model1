from .import forms
from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import redirect, render
#for email sending

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib import messages

User= get_user_model()

def signup_view(request):
    if request.method=='POST':
        next= request.GET.get('next')  #When a user needs to be redirected to a specific page after completing an action (such as logging in or signing up), developers often use the next parameter to specify the URL of the page to redirect to. This is useful for maintaining the user's intended destination after they've completed the action.
        
        form= forms.UserRegisterForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            password= form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            
            new_user= authenticate(email= user.email, password= password)
            login(request, new_user)
            
            if next:
                return redirect(next)
            else:
                return redirect('verify-email')
            
    else:
        form= forms.UserRegisterForm()
        
    context= {'form': form}        
    return render(request, 'signup.html', context)

def verify_email(request):
    if request.method == "POST":
        if request.user.email_is_verified != True:
            current_site = get_current_site(request)
            user = request.user
            email = request.user.email
            subject = "Verify Email"
            message = render_to_string('verify_email_message.html', {
                'request': request,
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            email = EmailMessage(
                subject, message, to=[email]
            )
            email.content_subtype = 'html'
            email.send()
            return redirect('verify-email-done')
        else:
            return redirect('signup')
    return render(request, 'verify_email.html')

def verify_email_done(request):
    return render(request, 'verify_email_done.html')


def verify_email_confirm(request, uidb64, token):
    print('hello')
    print(uidb64, token)
    next= request.GET.get('next')
    try:
        uid= force_str(urlsafe_base64_decode(uidb64))
        user= User.objects.get(pk=uid)
        
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user= None
        
    if user is not None and account_activation_token.check_token(user, token):
        user.email_is_verified= True
        user.save()
        messages.success(request, 'Your email has been verified')
        return redirect('signup')
    
    else:
        messages.warning(request, 'The link is invalid')
        
    return render(request, 'verify_email_confirm.html')

def verify_email_complete(request):
    return render(request, 'verify_email_complete.html')
            