from django.db import models


class Member(models.Model):

    username = models.CharField(max_length=30, null=False)
    dateOfBirth = models.DateField(max_length=8, null=False,default='YYYY-MM-DD')
    gender = models.DecimalField(decimal_places=2, max_digits=6,null=True)
    profileImage = models.ImageField(upload_to='profile_images', default=None)
    email = models.EmailField(max_length=254, default='unknown@unknown.com')

