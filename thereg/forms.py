from django import forms
from thereg.models import UserProfileInfo 
from thereg.models import Feedback
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('Institute','Department','Year','profile_pic')






class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = []