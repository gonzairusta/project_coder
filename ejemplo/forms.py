from django import forms
from ejemplo.models import Familiar, Mascota, Automovil

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'nacimiento']

class MascotaForm(forms.ModelForm):
  class Meta:
    model = Mascota
    fields = ['nombre', 'raza', 'edad']

class AutomovilForm(forms.ModelForm):
  class Meta:
    model = Automovil
    fields = ['marca', 'modelo', 'color']


