from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .import models
from .import forms
# Create your views here.

def show_cars(request):
    cars=models.Car.objects.all()
    return render(request, 'home.html', {'cars':cars})

class CarDetail(DetailView):
    model= models.Car
    template_name='details.html'
    # success_url= reverse_lazy('home')
    pk_url_kwarg='id'
    
    def post(self, request, *args, **kwargs):
        comment_form= forms.CommentForm(request.POST)
        car= self.get_object()
        
        if comment_form.is_valid():
            new_comment= comment_form.save(commit=False)
            new_comment.car= car
            new_comment.save()
            return redirect('detail', id=car.id)
        
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context=super().get_context_data(**kwargs)
        car= self.get_object()
        form=forms.CommentForm()
        comments= car.comment.all()
        
        context['form']= form
        context['comments']= comments
        return context
        
        
    
    
    
    # def form_valid(self, form):
    #     form.instance.car= self.get_object()
    #     return super().form_valid(form)
    
    # def get_context_data(self, *args, **kwargs):
    #     context= super().get_context_data(**kwargs)
    #     car= self.object 
    #     comments= car.comment.all()
        
    #     context['comments']= comments
    #     return context
    
    
    
# context= super().get_context_data(**kwargs)
#    post= self.object #post model er object
#    comments= post.comments.all()
#    comment_form= forms.CommentForm()
       
#    context['comments'] = comments
#    context['comment_form']= comment_form
#    return context
        

