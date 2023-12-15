from rest_framework import serializers
from conteudo.models.categoria import Categoria
from conteudo.models.conteudo import Conteudo

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ['titulo', 'descricao','tag','data_criacao','data_atualizacao']


class ConteudoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)

    class Meta:        
        model = Conteudo 
        fields = ['titulo', 'descricao', 'url', 'anexo', 'autor', 'categoria','data_criacao','data_atualizacao', ]


