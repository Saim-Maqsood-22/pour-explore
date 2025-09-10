from django.shortcuts import render, HttpResponseRedirect
from .forms import contactForm

# Create your views here.
def contactSubmit(request):
    if request.method == "POST":
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("Thanks/")
        
    else:
        form = contactForm()
    return render(request, "website/contact.html", {"form":form})

def Thanks(request):
    return render(request, "website/Thanks.html")