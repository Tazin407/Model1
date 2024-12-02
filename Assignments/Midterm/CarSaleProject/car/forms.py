from django import forms 
from .import models

class CommentForm(forms.ModelForm):
    class Meta:
        model=models.Comment
        fields=['text']
        labels={
            'text': 'Add Comment'
        }