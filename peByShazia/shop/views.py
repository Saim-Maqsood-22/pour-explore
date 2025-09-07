from django.shortcuts import render
from .models import products

# Create your views here.
product=products.objects.all()
context = {
    'products':product
}
def shop(request):
    return render(request, "shop/index.html", context)