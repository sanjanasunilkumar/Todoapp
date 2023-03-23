from django.db import models

class Products(models.Model):
    name=models.CharField(unique=True,max_length=200)
    description=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self) :
        return self.name