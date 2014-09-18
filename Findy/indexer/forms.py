#encoding:utf-8
from django import forms
from models import User
from models import IndexedPage

# Formulario de Usuario
class FormUser(forms.ModelForm):

	class Meta:
		model = User
		fields = '__all__'

# Formulario de Pagina a Indexar
class FormIndexedPage(forms.ModelForm):

	class Meta:
		model = IndexedPage
		fields = ('url',)