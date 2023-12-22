from django.forms import forms, ModelForm, CharField, TextInput, Textarea, BooleanField, CheckboxInput

from product.models import *


class VariantForm(ModelForm):
    class Meta:
        model = Variant
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'active': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'active'})
        }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title','sku','description']

class ProductVariantForm(ModelForm):
    class Meta:
        model = ProductVariant
        fields = ['variant_title','variant','product']

class ProductImageForm(ModelForm):
    class Meta:
        model = ProductImage
        fields = ['product','file_path']

class ProductVariantPriceForm(ModelForm):
    class Meta:
        model = ProductVariantPrice
        fields = ['product_variant_one','product_variant_two','product_variant_three','price','stock','product']

