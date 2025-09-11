from django import forms
from .models import Contact

class contactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ["customer_name", "customer_email", "message"]
        labels={
            'customer_name':'Your Name',
            'customer_email':'Your Email',
            'message':'Your Message'
        }
        widgets={
            'customer_name':forms.TextInput(attrs={
                'class':'w-screen p-3 bg-white outline-none',
                'placeholder':'Enter your name'
            }),
            'customer_email':forms.EmailInput(attrs={
                'class':'w-screen p-3 bg-white outline-none',
                'placeholder':'Enter your E-mail'
            }),
            'message':forms.Textarea(attrs={
                'class':'w-screen p-3 bg-white outline-none',
                'placeholder':'Enter your message',
                'rows':2,
            }),
        }
