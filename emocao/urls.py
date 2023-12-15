from django.urls import path, include

from emocao.api.viewsets import EmocaoViewSet
from .views import AtualizarEmocaoView, CriarEmocaoView, DetalharEmocaoView, ListarEmocoesView, PaginaEmocoes
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'emocao', EmocaoViewSet, basename='emocao')

urlpatterns = [
   path('PaginaEmocoes/', PaginaEmocoes.as_view(), name='PaginaEmocoes'),
   path('EnviarEmocao/', CriarEmocaoView.as_view(), name='EnviarEmocao'),
   path('ListarEmocoes/', ListarEmocoesView.as_view(), name='ListarEmocoes'),
   path('AtualizarEmocao/<int:id>/', AtualizarEmocaoView.as_view(), name='AtualizarEmocao'),
   path('DetalharEmocao/<int:id>/', DetalharEmocaoView.as_view(), name='DetalharEmocao'),
   path('', include(router.urls)),

]