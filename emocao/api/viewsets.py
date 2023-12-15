from crum import get_current_user
from django.core import serializers
from django.http import JsonResponse
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   RetrieveModelMixin, UpdateModelMixin)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from emocao.api.serializers import EmocaoSerializer
from emocao.models.emocao import Emocao



class EmocaoViewSet(   
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):

    permission_classes_by_action = {
        "create": [permissions.IsAuthenticated],
    }
    serializer_class = EmocaoSerializer
    #vai listar o curriculo daquele usuario.
    @action(detail=True, methods=["get"]) 
    def minhas_emocoes(self, request, *args, **kwargs):
        user = get_current_user()
        if user.is_authenticated:
            return Emocao.objects.filter(usuario_criacao=user)
        else:
            # Retorne um queryset vazio ou lide com isso de acordo com a lógica do seu aplicativo.
            return Emocao.objects.none()

    def get_queryset(self):
        user = get_current_user()
        if user.is_authenticated:
            return Emocao.objects.filter(usuario_criacao=user)
        else:
            # Retorne um queryset vazio ou lide com isso de acordo com a lógica do seu aplicativo.
            return Emocao.objects.none()
    
