from django.db import models

from accounts.models import User
# Create your models here.
class Lead(models.Model):

    name = models.CharField(max_length=200)

    email = models.EmailField(max_length=200,unique=True)

    phone = models.CharField(max_length=12,unique=True)

    company = models.CharField(max_length=200,null=True)

    SOURCE_CHOICES = (
        ("website","website"),
        ("social media","social media"),
        ("referral","referral"),
        ("advertisement","advertisement"),
        ("other","other")
    )

    source = models.CharField(max_length=200,choices=SOURCE_CHOICES,default="other")

    STATUS_CHOICES = (
        ("new","new"),
        ("contracted","contracted"),
        ("interested","interested"),
        ("converted","converted"),
        ("lost","lost")
    )

    status = models.CharField(max_length=200,choices=STATUS_CHOICES)

    description = models.TextField(null=True)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)