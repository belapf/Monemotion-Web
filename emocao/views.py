from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from datetime import date
from .models.emocao import Emocao
from .forms import EmocaoForm
from django.urls import reverse_lazy


# view para as emoções dos alunos
class PaginaEmocoesView(View):
    def get(self, request):
        emocoes = Emocao.objects.all()
        context = {"emocoes": emocoes}
        return render(request, "pagina_emocoes.html", context)


# view para a pagina sobre emoções
class PaginaEmocoes(View):
    def get(self, request):
        return render(request, "PaginaEmocoes.html")


# CRUD EMOÇÕES


import logging

logger = logging.getLogger(__name__)

@method_decorator(login_required, name='dispatch')
class CriarEmocaoView(CreateView):
    model = Emocao
    form_class = EmocaoForm
    template_name = 'EnviarEmocao.html'
    success_url = reverse_lazy('perfil')

    def form_valid(self, form):
        try:
            form.instance.usuario_criacao = self.request.user
            result = super().form_valid(form)
            logger.info(f'Dados salvos com sucesso: {form.instance}')
            return result
        except Exception as e:
            logger.error(f'Erro ao salvar dados: {e}')
            raise
    

@method_decorator(login_required, name='dispatch')
class ListarEmocoesView(ListView):
    model = Emocao
    template_name = 'ListarEmocoes.html'
    context_object_name = 'emocoes'

    def get_queryset(self):
        return Emocao.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class AtualizarEmocaoView(UpdateView):
    model = Emocao
    form_class = EmocaoForm
    template_name = 'EnviarEmocao.html'

    def get(self, request, *args, **kwargs):
        emocao = self.get_object()
        hoje = date.today()
        if emocao.data != hoje:
            return render(
                request,
                "DetalharEmocao.html",
                {"error_message": "Você só pode editar emoções criadas no mesmo dia."},
            )
        return super().get(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class DetalharEmocaoView(DetailView):
    model = Emocao
    template_name = 'DetalharEmocao.html'
    context_object_name = 'emocao'