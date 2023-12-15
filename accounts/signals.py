from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

User = get_user_model()

@receiver(post_save, sender=User)
def assign_permission(sender, instance, **kwargs):
    if instance.role == User.PSICOLOGO:
        permission_codename = 'acessar_paginas_profile_psicologo'
    elif instance.role == User.ALUNO:
        permission_codename = 'acessar_paginas_profile_estudante'
    elif instance.role == User.PROFESSOR:
        permission_codename = 'acessar_paginas_profile_professor'
    else:
        return  # Não faz nada se a role não for uma das esperadas

    permission = Permission.objects.get(codename=permission_codename)
    if permission not in instance.user_permissions.all():
        instance.user_permissions.add(permission)