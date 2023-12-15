from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import UserProfile

from django.utils import timezone
import datetime
from django.views.generic import TemplateView
from django.db.models import Count
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import (LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView, PasswordChangeView)
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DeleteView, RedirectView, RedirectView, DetailView, UpdateView, ListView
from accounts.forms import UserAdminCreationForm, UserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import ClasseSocial, Etnia, User, UserProfile
from django.contrib.auth import logout
from core.models.ano import Ano
from datetime import datetime, timedelta
from core.models.curso import Curso
from emocao.models import Emocao
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.db.models import Count
from .models import RelatorioPsicologico
from .forms import RelatorioPsicologicoForm


#classe utilizada para fazer o login no sistema 
class UserLogin(SuccessMessageMixin, LoginView):
    template_name = 'admin/login/login.html'

    # def form_invalid(self, form):
    #     # Verificar se apenas a senha está errada
    #     if 'password' in form.errors and not form.errors.get('username'):
    #         form.add_error('password', 'Senha incorreta. Verifique novamente.')
    #     return super().form_invalid(form)

"""
class RegisterView(CreateView):
    model = User
    template_name = 'admin/register/new_user.html'
    form_class = UserForm
    success_url = reverse_lazy('entrar')
"""
"""
class ProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'admin/user/profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        return self.request.user.userprofile
"""

# class CreateUserView(View):
#     def get(self, request):
#         form = UserForm(initial={'role': User.ALUNO})  # Defina o papel 'Aluno' como valor inicial do campo role
#         return render(request, "admin/register/new_user.html", {'form': form})

#     def post(self, request):
#         form = UserForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)  # Crie uma instância do usuário a partir do formulário, sem salvar no banco de dados ainda
#             user.role = request.POST.get('role')  # Atribua o papel com base na seleção do usuário no campo role
#             user.save()  # Agora salve o usuário no banco de dados
#             form = UserForm()  # Crie um novo formulário em branco
#         else:
#             print(form.errors)
             

#         return render(request, "admin/login/login.html", {'form': form})
from django.contrib import messages

class CreateUserView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'admin/register/new_user.html'
    success_url = reverse_lazy('entrar')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['etnias'] = list(Etnia.objects.all())
        context['classes_sociais'] = list(ClasseSocial.objects.all())
        context['cursos'] = list(Curso.objects.all())
        context['anos'] = list(Ano.objects.all())
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        # Defina o papel do usuário como 'Aluno'
        user.role = User.ALUNO
        # user.set_password(form.cleaned_data['password'])  # Defina a senha usando set_password
        user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        # Adicione detalhes sobre os erros ao form.errors
        error_details = form.errors.as_text()

        print(f'Erro ao cadastrar usuário. Detalhes: {error_details}')
        
        # Adicione uma mensagem de erro com os detalhes
        messages.error(self.request, f'Erro ao cadastrar usuário. Detalhes: {error_details}')

        # Retorne a resposta padrão para formulários inválidos
        return super().form_invalid(form)


class LogoutView(LoginRequiredMixin, RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(self, request, *args, **kwargs)
    

class ProfileView(LoginRequiredMixin, View):
    template_name = 'admin/user/profile.html'

    def get(self, request, *args, **kwargs):
        # Obtém o UserProfile associado ao usuário logado
        user_profile = UserProfile.objects.get(user=request.user)
        users = User.objects.all()

        # Verifica se o usuário logado é o mesmo do perfil
        if user_profile:
            # Realize o restante da lógica para obter os dados para o gráfico
            end_date = timezone.now()
            start_date = end_date - timedelta(days=7)

            # Adicione prints para depuração
            print(f"Usuario logado: {request.user}")
            print(f"Data inicial: {start_date}, Data final: {end_date}")

            # Adicione um filtro mais amplo para depuração
            todas_emocoes = Emocao.objects.filter(data_criacao__gte=start_date, data_criacao__lte=end_date)
            print(f"Todas as emoções: {todas_emocoes}")

            # Adicione prints para depurar emoções específicas do usuário logado
            emocoes_do_usuario = Emocao.objects.filter(usuario_criacao=request.user, )
            print(f"Emoções do usuário logado: {emocoes_do_usuario}")

            emocoes_count = emocoes_do_usuario.values('tipo_emocao').annotate(count=Count('tipo_emocao'))
            print(f"Contagem de emoções do usuário logado: {emocoes_count}")

            emocao_choices = Emocao.ROLE_CHOICES
            # Extraia os rótulos das opções
            labels = [choice[1] for choice in emocao_choices]
            
            # Use emocoes_count para gerar os dados para o gráfico
            data = [next((emo['count'] for emo in emocoes_count if emo['tipo_emocao'] == choice[0]), 0) for choice in emocao_choices]

            # Passe os dados para o contexto e renderize o modelo
            context = {
                'user_profile': user_profile,
                'labels': labels,
                'data': data,
                'users': users,
                'emocoes_do_usuario': emocoes_do_usuario
            }

            return render(request, self.template_name, context)
        
        else:
            return HttpResponseForbidden("Você não tem permissão para acessar este perfil.")
        
class EmocaoDeleteView(DeleteView):
    model = Emocao
    template_name = 'admin/user/emocao_confirm_delete.html'
    success_url = reverse_lazy('perfil')
        
class UpdateProfileView(UpdateView):
    template_name = 'admin/user/profile.html'
    model = User
    fields = [
            'first_name', 'last_name', 'etnia', 'classe_social', 'religiao',
            'curso', 'matricula', 'ano', 'email', 'telefone', 'cep',
            'cidade', 'rua', 'bairro', 'logadouro', 'localidade', 'numero',
        ]
    success_url = reverse_lazy('perfil')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(User, usuario=self.request.user) #Não precisa colocar o id na url, pega pelo perfil do user
        return self.object

class RelatorioPsicologicoListView(ListView):
    model = RelatorioPsicologico
    template_name = 'profile.html'
    context_object_name = 'relatorios'


        
class PasswordReset(SuccessMessageMixin, PasswordResetView):
    template_name = 'admin/user/password-reset.html'


class PasswordResetDone(SuccessMessageMixin, PasswordResetDoneView):
    template_name = 'admin/user/password_reset_done.html'


class PasswordResetConfirm(SuccessMessageMixin, PasswordResetConfirmView):
    template_name = 'admin/user/password_reset_confirm.html'


class PasswordResetCompleteView(SuccessMessageMixin, PasswordResetCompleteView):
    success_message = 'Senha Alterada com sucesso!'
    template_name = 'admin/login/login.html'


class PasswordChange(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    template_name = 'admin/user/password_change.html'
    success_message = "Senha alterada com sucesso!"

