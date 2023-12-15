from rest_framework import serializers

from emocao.models.emocao import Emocao

class EmocaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Emocao
        fields = ['motivo']