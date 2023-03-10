from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

class DateInput(forms.DateInput):
	input_type = 'date'

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2','email')


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class MascotasForm(forms.ModelForm):
	class Meta:
		model =  Mascotas
		fields = ['namePet', 'infoPet', 'agePet', 'typePet', 'imgPet', 'genderPet']
		widgets = {'agePet' : DateInput()}

#class PerdidosForm(forms.Form):
#	infoLost=forms.CharField(label="Descripción",required=True)
#	dateLost=forms.DateField(label="Fecha de desaparición",required=True)
#	ubiLost=forms.CharField(label="Ubicación de pérdida",required=True)
	
class PerdidosForm(forms.ModelForm):
	class Meta:
		model = Perdidos
		fields = ['infoLost', 'dateLost', 'ubiLost']
		widgets = {'dateLost' : DateInput()}

class EncuentrosForm(forms.ModelForm):
    class Meta:
        model = Encuentros
        fields = ['typeFind', 'imgFind', 'infoFind', 'genderFind', 'ubiFind']
           
class CorreoForm(forms.ModelForm):
    class Meta:
        model = Correo
        fields = ['asunto', 'mensaje']
        