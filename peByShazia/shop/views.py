from django.shortcuts import render
from .models import products

# Create your views here.
product=products.objects.all()
def shop(request):
    return render(request, "shop/index.html", {"products":product})