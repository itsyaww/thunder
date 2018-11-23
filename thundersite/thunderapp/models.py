from django.db import models


class Member(models.Model):

    username = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30,default='0')
    gender = models.CharField(max_length=7, null=True)
    dateOfBirth = models.CharField(max_length=10)
    email = models.EmailField(max_length=254, default='unknown@unknown.com')
    profileImage = models.ImageField(upload_to='profile_images', default=None)

