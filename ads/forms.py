from django import forms
from .models import Ad

class PostAdForm(forms.ModelForm):
    class Meta:
        model = Ad
        image = forms.FileField(required=False)
        fields = '__all__'
