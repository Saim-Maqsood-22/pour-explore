from django.db import models

# Create your models here.
class products(models.Model):
    image=models.ImageField(upload_to='media')
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=50)
    price=models.PositiveIntegerField(null=False)

    class Meta:
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return self.name