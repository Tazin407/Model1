from django.shortcuts import render
from .forms import contactForm,studentData
# Create your views here.

def account(request):
    if(request.method == 'POST'):
        name= request.POST.get('name')
        email= request.POST.get('email')
        select= request.POST.get('size')
        
        return render(request,'account.html', {"name": name, "email": email, "select":select})
    

def form(request):
    print(request.POST)
    return render(request, 'form.html')

def djangoForm(request):
    
    if request.method=='POST':
        form= contactForm(request.POST, request.FILES)
        print(request.POST)
        
        if form.is_valid():
            file= form.cleaned_data["file"]
            if file:
                with open('./app/pictures/' + file.name, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                print(form.cleaned_data)
            
            else:
                print('No file found')
                
            # return render(request, 'account.html', {"form": form})
            
    else:
        form= contactForm()
        
    return render(request, 'djangoForm.html', {"form": form})

def StudentData(request):
    if request.method=="POST":
        form= studentData(request.POST)
        print(request.POST)
        return render(request, 'djangoForm.html', {"form": form})
    else:
        form= studentData()
        
    return render(request, 'djangoForm.html', {"form": form})

