from django.db import models


class User(models.Model):

    name = models.CharField(max_length=30, null=False)
    age = models.DecimalField(decimal_places=2, max_digits=6,null=True)
    gender = models.DecimalField(decimal_places=2, max_digits=6,null=True)

