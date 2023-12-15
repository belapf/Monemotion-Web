from django.views.generic.list import ListView
from django.shortcuts import render
from django.views import View
from conteudo.models.conteudo import Conteudo
from .models import Conteudo, Categoria
import re

class PaginaNoticiasView(ListView):
    model = Conteudo
    template_name = 'PaginaNoticias.html'

    def get_queryset(self):
        # Selecionar as últimas 3 notícias com categoria 'Noticia'
        return Conteudo.objects.filter(categoria__tag='Noticia').order_by('-data_criacao')[:3]

class VideosPodcastsView(ListView):
    model = Conteudo
    template_name = "videos_podcasts.html"
    paginate_by = 1

    def get_queryset(self):
        # Obtém as categorias 'Video' e 'Podcast' do modelo Categoria
        categorias_videos_podcasts = Categoria.objects.filter(
            tag__in=[Categoria.VIDEO, Categoria.PODCAST]
        )

        # Filtra os conteúdos com base nas categorias desejadas
        queryset = Conteudo.objects.filter(categoria__in=categorias_videos_podcasts)

        # Itera sobre os objetos do queryset e adiciona os valores dos campos embed_link
        for conteudo in queryset:
            match = re.search(r'v=([^&]+)', conteudo.url)
            if match:
                video_id = match.group(1)
                conteudo.embed_link = f"https://www.youtube.com/embed/{video_id}"

        return queryset


    
