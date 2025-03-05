from django import forms
from .models import UserProfile
from .models import UploadedImage

class ImageUploadForm(forms.ModelForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    height = forms.FloatField(help_text="Enter height in meters")
    weight = forms.FloatField(help_text="Enter weight in kg")

    class Meta:
        model = UploadedImage
        fields = ['image', 'birthdate', 'height', 'weight']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'birth_date', 'height', 'weight', 'image']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
