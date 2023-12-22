from django.shortcuts import redirect,render
from django.views import generic

from product.models import *


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context

def create_product_image(request):
    if request.method == "POST":
        form = ProductImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            redirect('list.product')
    else:
        form = ProductImageForm()
    return render(request,'products/create.html',{'form':form})

def create_product_variant(request):
    if request.method == "POST":
        form = ProductVariantForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('list.product')
    else:
        form = ProductImageForm()
    return render(request,'products/create.html',{'form':form})

def create_product_variant_price(request):

    if request.method == "POST":
        form = ProductVariantPriceForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('list.product')
    else:
        form = ProductVariantPriceForm()
    return render(request,'products/create.html',{'form':form})