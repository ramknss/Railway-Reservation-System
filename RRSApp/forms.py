from .models import User,Train,Rform,Story
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms

class AusForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model = User
		fields = ["username"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Username",
			}),
		}

class UsuserForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model = User
		fields = ["username","first_name","last_name","mble","gdr"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			#"readonly":"true",
			"placeholder":"User Name",
			"primary_key":"true",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Last Name",
			}),
		"mble":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Mobile Number",
			}),
		"gdr":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}
class UspForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email","mble","gdr","pfimg"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":"true",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Last Name",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Mailid",
			}),
		"mble":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Mobile Number",
			}),
		"gdr":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class ChgPwdForm(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Old Password"}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"New Password"}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model = User
		fields = "__all__"



class AddTrainForm(forms.ModelForm):
    deptimesrc = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(attrs={'class': 'form-control my-2', 'type': 'datetime-local'}),
    )
    arrtimedes = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(attrs={'class': 'form-control my-2', 'type': 'datetime-local'}),
    )
    
    class Meta:
        model = Train
        fields = ["trainnum", "traintype", "trainsrc", "traindes","deptimesrc","arrtimedes","ticket_price"]
        widgets = {
            'trainnum': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Train Number', 'primary_key': 'true'}),
            'trainsrc': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Train Starting Point'}),
            'traindes': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Train Ending Point'}),
            'traintype': forms.Select(attrs={'class': 'form-control my-2'}),
        }



class Rtform(forms.ModelForm):
	class Meta:
		model = Rform 
		fields = ["usname","name","pno"]
		widgets = {
		"usname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Username of your account",
			"primary_key":"true",
			}),
		"name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Name of the Passenger",
			}),
		"pno":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Phone Number",
			}),
		}
		
class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['Title', 'writername', 'story']
        widgets = {
            "Title": forms.TextInput(attrs={
                #"class": "form-control my-2",
                "placeholder": "Title",
            }),
            "writername": forms.TextInput(attrs={
                #"class": "form-control my-2",
                "placeholder": "Name",
            }),
			
        }


