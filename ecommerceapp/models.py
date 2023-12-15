from django.db import models
from django.contrib.auth.models import User

class category(models.Model):
    category_name=models.CharField(max_length=255)


class product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.ForeignKey(category, on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to="images/",null=True)

class member(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    image=models.ImageField(upload_to="images/",null=True)
    
class cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(product, on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(default=1)
    