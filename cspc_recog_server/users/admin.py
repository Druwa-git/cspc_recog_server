"""
from django.contrib import admin
from .models import Group, Profile

admin.site.register(Profile)
admin.site.register(Group)
# Register your models here.
"""
# api/admin.py
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, Group


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profile"

class GroupInline(admin.StackedInline):
    model = Group
    can_delete = False
    verbose_name_plural = "group"


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,
               GroupInline,
               )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Group)