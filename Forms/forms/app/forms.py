from django import forms
from django.core import validators

class contactForm(forms.Form):
    name= forms.CharField(label= 'username: ', widget=forms.Textarea, help_text= "text must be within 70 letters")
    email= forms.EmailField(label='email')
    age= forms.IntegerField(label='age')
    birthday= forms.DateField(widget=forms.DateInput(attrs= {'type':'date'}))
    appointment= forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    check= forms.BooleanField(required=False)
    
    SIZES=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size= forms.ChoiceField(choices=SIZES, widget=forms.RadioSelect)
    
    # Multiple choices
    
    CHOICES=[('P', 'Pizza'), ('B', 'Burger'), ('M', 'Mashroom')]
    food= forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple)
    
    file= forms.FileField(required=False)
    
    
# class studentData(forms.Form):
#     name=forms.CharField(widget=forms.TextInput)
#     email=forms.EmailField()
    
#     def clean(self):
        
#         # valname= self.cleaned_data['name']
#         # if len(valname) < 10:
#         #     raise forms.ValidationError("Name must contain 10 letters")
        
#         # else:
#         #     return valname
        
        
#         cleaned_data= super().clean()
#         valname= self.cleaned_data.get('name')
#         valemail= self.cleaned_data.get('email')
#         if len(valname) < 10:            
#             raise forms.ValidationError("Name must contain 10 letters")
        
#         if '.com' not in valemail:
#             raise forms.ValidationError("Email must contain .com")

def emailChecker(email):
    if '.com' not in email:
        raise forms.ValidationError("Enter a valid email address")

# class studentData(forms.Form):
#     name= forms.CharField(validators=[validators.MinLengthValidator(10, message="Name should have at least 10 letters")])
#     email= forms.EmailField(validators=[validators.EmailValidator, emailChecker])
#     age= forms.IntegerField(validators=[validators.MinValueValidator(17, message="age must be at least 17"),validators.MaxValueValidator(34)])

class studentData(forms.Form):
    name= forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput)
    passwordd= forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    
    def clean(self):
        cleaned_data= super().clean()
        valPass= self.cleaned_data['password']
        valPass2= self.cleaned_data['passwordd']
        
        if valPass != valPass2:
            raise forms.ValidationError("passwords don't match")