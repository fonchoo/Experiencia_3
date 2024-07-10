from django import forms
from .models import Producto
from django.contrib.auth.models import User
from django import forms
from .models import CustomUser
from django import forms
from .models import DetalleCompra


class CustomUserCreationForm(forms.ModelForm):
    password_confirm = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password', 'password_confirm']
        widgets = {
            'password': forms.PasswordInput(),
            'password_confirm': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Excluir date_joined del formulario
        self.fields['date_joined'].widget = forms.HiddenInput()
        self.fields['date_joined'].disabled = True  # Opcionalmente, puedes deshabilitar el campo

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password_confirm

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id_producto', 'nombre', 'descripcion', 'imagen', 'precio', 'stock', 'categoria']
        

class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name']

        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electronico',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'readonly': 'readonly'}),
        }
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if CustomUser.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('El emmail ya esta en uso.')
            return email

class AgregarAlCarritoForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = ['producto', 'cantidad']

    def __init__(self, *args, **kwargs):
        super(AgregarAlCarritoForm, self).__init__(*args, **kwargs)
        self.fields['cantidad'].widget.attrs.update({'min': 1, 'value': 1})

class ProductoSearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)


        
        
        


        

