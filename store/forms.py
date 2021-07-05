from django import forms
from django.forms import widgets
from .models import Product


class ArticuloForm(forms.ModelForm):
        
    class Meta:
        model = Product
        fields = ['title', 'image', 'description', 'price', 'category']
        labels={
            'title': 'Titulo',
            'image': 'Imagen',
            'description': 'Descripción',
            'category': 'Categoria',
            'price': 'Precio',
        }

        widgets= {
            'description': forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'Descripción'}),
            'title': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Título de producto'})
        }

class UpdateArticuloForm(forms.ModelForm):
        
    class Meta:
        model = Product
        fields = ['title', 'image', 'description', 'price', 'category']
        labels={
            'title': 'Titulo',
            'image': 'Imagen',
            'description': 'Descripción',
            'category': 'Categoria',
            'price': 'Precio',
        }

        widgets= {
            'description': forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'Descripción'}),
            'title': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Título de producto'})
        }    
    def save(self):
        product = self.instance
        product.title = self.cleaned_data['Titulo']
        product.description = self.cleaned_data['Descripcion']
        product.category = self.cleaned_data['Categoria']
        product.price = self.cleaned_data['Precio']

        if self.clenead_data['image']:
            image = self.cleaned_data['Imagen']
        product.save()
        return product
