from django.db import models
from django.utils import timezone
# Create your models here.
class Contact(models.Model):
    customer_name=models.CharField(max_length=15)
    customer_email=models.EmailField(blank=False, null=False)
    message=models.TextField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name='contact'
        verbose_name_plural='contact'
    
    def __str__(self):
        return f"sent by: {self.customer_name} sent on {timezone.localdate()}"