from django.db import models


class Order(models.Model):
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    description = models.TextField()
    address_from = models.CharField(max_length=150, null=True)
    address_to = models.CharField(max_length=150, null=True)


class LegalServices(models.Model):
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    description = models.TextField()
