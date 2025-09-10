from django import forms
from .models import Contact

class contactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ["customer_name", "customer_email", "message"]
