
from django import forms
from .models import Canais

class CanalForm(forms.Form):
    nome_video = forms.CharField(label='Nome')
    select = forms.ModelChoiceField(queryset=Canais.objects.all())
