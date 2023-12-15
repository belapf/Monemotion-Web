from accounts.models import User
from rest_framework import permissions


class IsPsicologo(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Verifica se o usuário é um psicólogo
        if request.user.role == User.PSICOLOGO:
            return True
        return False

