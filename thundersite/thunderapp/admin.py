from django.contrib import admin
from .models import Member, Hobby, Message


# Register your models here.
class Admin(admin.ModelAdmin):
    list_display = ['id','firstName','lastName','username', 'password','gender','dateOfBirth','email','profileImage']
    list_editable = ['password','gender','dateOfBirth','email','profileImage']
    list_display_links = ['username']


admin.site.register(Member, Admin)
admin.site.register(Hobby)
admin.site.register(Message)
#username: admin
#password: admin
