from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import UserAdminCreationForm
from .models import User, UserProfile, Etnia, ClasseSocial


@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = UserAdminCreationForm

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2','telefone', 'is_staff', 'role'),
        }),
    ) 
    add_form_template = None


    list_display = [
        'id',
        'username',
        'first_name',
        'last_name',
        'role',
        'image',
    ]

    list_filter = [
        'email',
        'first_name',
        'last_name',
    ]

    search_fields = [
        'email',
        'first_name',
        'last_name',
    ]



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'user',
    ]



@admin.register(Etnia)
class Etnia(admin.ModelAdmin): 
        list_display = [
        'id',
        'nome',
    ]


@admin.register(ClasseSocial)
class ClasseSocial(admin.ModelAdmin): 
        list_display = [
        'id',
        'nome',
    ]