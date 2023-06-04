# from django.forms import modelForm
# from .models import order
from django.contrib.auth.models  import User
from django.contrib.auth.forms import UserCreationForm
# class orderForm(modelForm):
#     class Meta :
#         model=order
#         fields="__all__"
from django import forms
from .models import Stage

class CreateNewUser(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'subject', 'message']
class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ('description', 'image', 'poste')
class StageForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Stage
        fields = ('description', 'image', 'poste')
