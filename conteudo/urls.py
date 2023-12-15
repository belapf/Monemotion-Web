from django.urls import path, include
from conteudo.api.viewsets import ConteudoViewSet, CategoriaViewSet
from conteudo.views import PaginaNoticiasView, VideosPodcastsView
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'conteudos', ConteudoViewSet, basename='conteudos')
router.register(r'categorias', CategoriaViewSet, basename='categorias')


urlpatterns = [
   path('VideosPodcasts/', VideosPodcastsView.as_view(), name='VideosPodcasts'),
   path('PaginaNoticias/', PaginaNoticiasView.as_view(), name='PaginaNoticias'),
   path('', include(router.urls)),

] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    