from django import forms
from appsite.models import Users 

class Prosignup(forms.Form):
    first_name =forms.CharField(label='Your name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    email =forms.EmailField()  
    city = forms.CharField(required = False, )
    country = forms.CharField(required = False, )
    password = forms.CharField(widget = forms.PasswordInput)
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError("Password is too short. Password should be at least 8 characters.")
            print("wrong pass length" ) 
           
        return password
    
class Usersignup(forms.ModelForm):

    class Meta:
        model = Users
        fields = ('username', 'password', 'email', 'firstname', 'lastname', 'country', ) 
        
         
# class Usersignup(forms.Form):
#     first_name =forms.CharField(label='Your name', max_length=100)
#     last_name = forms.CharField(label='Last name', max_length=100)
#     # email =forms.EmailField() associate gmail
#     city = forms.CharField(required = False, )
#     country = forms.CharField(required = False, )
#     password = forms.CharField(widget = forms.PasswordInput)


   