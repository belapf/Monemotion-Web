from django.core import serializers
from django.http import JsonResponse
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   RetrieveModelMixin, UpdateModelMixin)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from conteudo.api.serializers import CategoriaSerializer, ConteudoSerializer
from conteudo.models.categoria import Categoria

from conteudo.models.conteudo import Conteudo



class ConteudoViewSet(   
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    # UpdateModelMixin,
    GenericViewSet,
):

    permission_classes_by_action = {
        "create": [permissions.IsAuthenticated],
    }
    serializer_class = ConteudoSerializer

    def get_queryset(self):
        return Conteudo.objects.all()

    def create(self, request, *args, **kwargs):
        # Verificar se o usuário tem a função (role) "PSICOLOGO"
        if request.user.has_role('PSICOLOGO'):
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Apenas usuários com a função (role) 'PSICOLOGO' podem criar categorias."}, status=status.HTTP_403_FORBIDDEN)


    def get_permissions(self):
        try:
            # Verificar se self.action está definido no dicionário permission_classes_by_action
            if self.action in self.permission_classes_by_action:
                return [
                    permission()
                    for permission in self.permission_classes_by_action[self.action]
                ]
            else:
                # Ação não definida, retornar permissões padrão (por exemplo, IsAuthenticated)
                return [
                    permission()
                    for permission in self.permission_classes_by_action["default"]
                ]
        except KeyError:
            # Se ocorrer um erro, retornar uma lista vazia de permissões
            return []


class CategoriaViewSet(   
    ListModelMixin,
    GenericViewSet,
):

    permission_classes_by_action = {
        "create": [permissions.IsAuthenticated],
    }
    serializer_class = CategoriaSerializer

    def get_queryset(self):
        return Categoria.objects.all()


    def create(self, request, *args, **kwargs):
        # Verificar se o usuário tem a função (role) "PSICOLOGO"
        if request.user.has_role('PSICOLOGO'):
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Apenas usuários com a função (role) 'PSICOLOGO' podem criar categorias."}, status=status.HTTP_403_FORBIDDEN)


    def get_permissions(self):
        try:
            # Verificar se self.action está definido no dicionário permission_classes_by_action
            if self.action in self.permission_classes_by_action:
                return [
                    permission()
                    for permission in self.permission_classes_by_action[self.action]
                ]
            else:
                # Ação não definida, retornar permissões padrão (por exemplo, IsAuthenticated)
                return [
                    permission()
                    for permission in self.permission_classes_by_action["default"]
                ]
        except KeyError:
            # Se ocorrer um erro, retornar uma lista vazia de permissões
            return []