from django import forms 


allowed= ['2003','2004', '2005']
color= [
    ('blue','Blue'),
    ('green', 'Green'),
    ('brown', 'Brown')
]
class Client(forms.Form):
    name= forms.CharField() 
    email= forms.EmailField()
    Birthday= forms.DateField(label='BirthDate', widget=forms.SelectDateWidget(years=allowed))
    
    JoiningDate= forms.DateTimeField(widget=forms.NumberInput(attrs={'type':'date'}))
    
    agree= forms.BooleanField(help_text='Do you agree to our rules ?')
    
    favcol= forms.MultipleChoiceField(label='Favourite Color', choices=color,
                                      widget= forms.CheckboxSelectMultiple)
    
    comment= forms.CharField(widget=forms.Textarea(attrs={'rows':3}))#This enables multiline input
                                    #3 line text show korbe. bakita dekte hoile scroll lagbe
                                    
