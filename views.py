from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def product_html(request):
    template = loader.get_template('product.html')
    return render(request.template)
# Create your views here.
