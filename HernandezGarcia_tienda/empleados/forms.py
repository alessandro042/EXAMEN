from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre_completo', 'sueldo', 'departamento']

    def clean_sueldo(self):
        sueldo = self.cleaned_data.get('sueldo')
        if sueldo <= 0.0 or sueldo > 12000.0:
            raise forms.ValidationError('El sueldo debe estar entre 0.0 y 12000.0')
        return sueldo