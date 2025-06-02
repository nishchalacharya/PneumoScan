from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
from .models import Profile,xray_image,contact_us

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
  
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
     
            
        
        
class LoginForm(forms.Form):
    username=forms.CharField(max_length=150)
    password=forms.CharField(widget=forms.PasswordInput())   
         
         
class ProfileForm(forms.Form):
    class Meta:
        model=Profile
        fields=['is_doctor','phoneno','profile_pic']         
    
class Xrayimage(forms.ModelForm):
    class Meta:
        model=xray_image
        # fields=['xray_image','xray_author']
        fields=['xray_image']
        
        
class Feedbackpage(forms.ModelForm):
    class Meta:
        model= contact_us  
        fields='__all__'     
        
        
        
# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model=User        
        