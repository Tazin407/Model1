from django.shortcuts import render,redirect
from .import forms
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def profile(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form= forms.UpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request,'Account updated successfully')
                form.save()
        
        else:   
            form = forms.UpdateForm(instance=request.user)
        return render(request, 'profile.html',{'form': form})
    
    else:
        return redirect('signup')

def signup(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form= forms.RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request,'Account created successfully')
                messages.info(request,'Hello')
                messages.warning(request,'Something is wrong')
                print(form.cleaned_data)
                form.save()
                return redirect('login')
                # return render(request, 'home.html',{'form': form})
        
        else:   
            form = forms.RegisterForm()
        return render(request, 'signup.html',{'form': form})
    
    else:
        return render(request, 'profile.html', {'user': request.user})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form= AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name=form.cleaned_data['username']
                userpass= form.cleaned_data['password']
                
                user= authenticate(username=name, password= userpass)
                if user is not None:
                    login(request, user)
                    # print(form.cleaned_data)
                    return redirect('profile')
            
        else:
            form = AuthenticationForm()
        return render(request, './login.html', {'form': form})
    
    else:
        return render(request, './profile.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def change_pass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = PasswordChangeForm( user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
                
        else:
            form= PasswordChangeForm(user=request.user)
            
        return render(request, 'change_pass.html',{'form':form})
    
    else:
        return redirect('login')
    
def change_pass2(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = SetPasswordForm( user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
                
        else:
            form= SetPasswordForm(user=request.user)
            
        return render(request, 'change_pass.html',{'form':form})
    
    else:
        return redirect('login')
    
def change_data(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form= forms.UpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                
                form.save()
        
        else:   
            form = forms.UpdateForm()
        return render(request, 'profile.html',{'form': form})
    
    else:
        return redirect('signup')