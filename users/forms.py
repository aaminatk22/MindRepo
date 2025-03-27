from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms
from .models import Profile



class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date', 'profile_picture']


    def clean_profile_picture(self):
        picture = self.cleaned_data.get('profile_picture')
        if picture:
            if picture.size > 2*1024*1024:  # 2MB limit
                raise forms.ValidationError("Image file too large ( > 2MB )")
            return picture
        return None