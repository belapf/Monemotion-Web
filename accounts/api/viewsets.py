from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from accounts.api.serializers import UserProfileSerializer, UsuarioSerializer
from accounts.models import User
from rest_framework import viewsets

from accounts.permission import IsPsicologo

class UsuarioViewSet(viewsets.ModelViewSet):
    
    serializer_class = UsuarioSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'list', 'partial_update']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
    

    @action(detail=False, methods=["post"])
    def create_aluno(self, request, *args, **kwargs):
        # Validação dos dados da solicitação
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Definir o valor do campo role como ALUNO
        serializer.validated_data["role"] = User.ALUNO

        # Criação do aluno
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    # @action(detail=False, methods=["get"])
    def list(self, request, *args, **kwargs):
        if request.user.role == User.PSICOLOGO:
            # Filtrar os usuários com role "aluno"
            queryset = self.filter_queryset(self.get_queryset().filter(role=User.ALUNO))
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        # Verificar se o usuário é o próprio usuário ou um psicólogo
        if request.user == instance or IsPsicologo().has_object_permission(request, self, instance):
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



class UserProfileViewSet(viewsets.ModelViewSet):
    
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()


    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'list', 'partial_update']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]