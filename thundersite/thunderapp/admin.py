from django.contrib import admin
from .models import Member


# Register your models here.
class Admin(admin.ModelAdmin):
    list_display = ['username', 'password','gender','dateOfBirth','email']
    list_editable = ['password','gender','dateOfBirth','email']
    list_display_links = ['username']


admin.site.register(Member, Admin)
