from rest_framework import serializers

from accounts.models import User, UserProfile


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'telefone', 'cep', 'cidade', 'rua', 'bairro', 'logadouro', 'numero', 'image']



class UserProfileSerializer(serializers.ModelSerializer):
    user = UsuarioSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ['user']

