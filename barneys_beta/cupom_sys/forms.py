from django import forms
from django.forms import ModelForm
from .models import *

class PostForm(forms.ModelForm):
	class Meta:
		model = Promotion
		fields = [
		    "título",
		    "quantidade",
		    "preço_normal",
		    "preço_promocional",
		    "status",
		    "horário_de_consumo",
		    "regras_gerais",
		    "descrição",
		]
