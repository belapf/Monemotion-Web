from django.contrib.auth.forms import UserCreationForm
from .models import User, RelatorioPsicologico
from django import forms


class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        # fields= ('email','first_name','last_name')
        fields = '__all__'

class RelatorioPsicologicoForm(forms.ModelForm):
    class Meta:
        model = RelatorioPsicologico
        fields = ['titulo', 'imagem', 'turma', 'data_hora', 'relatorio']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'turma': forms.Select(attrs={'class': 'form-control'}),
            'classe_social': forms.Select(attrs={'class': 'form-control'}),
            'religiao': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UserForm(forms.ModelForm):
    ROLE_CHOICES = (
        (User.ALUNO, 'Aluno'),
    )

    role = forms.ChoiceField(label='Role', choices=ROLE_CHOICES, initial=User.ALUNO, widget=forms.HiddenInput())
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'etnia', 'classe_social', 'religiao',
            'curso', 'matricula', 'ano', 'email', 'telefone', 'cep',
            'cidade', 'rua', 'bairro', 'logadouro', 'localidade', 'numero',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'etnia': forms.Select(attrs={'class': 'form-control'}),
            'classe_social': forms.Select(attrs={'class': 'form-control'}),
            'religiao': forms.TextInput(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'rua': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'logadouro': forms.TextInput(attrs={'class': 'form-control'}),
            'localidade': forms.Select(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                self.add_error('password2', 'As senhas não coincidem. Por favor, tente novamente.')

        return cleaned_data

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     domain = email.split('@')[1]
    #     if domain not in ['escolar.ifrn.edu.br', 'academico.ifrn.edu.br']:
    #         raise forms.ValidationError("Você precisa usar um e-mail com domínio 'escolar.ifrn.edu.br' ou 'academico.ifrn.edu.br'.")
    #     return email



    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = self.cleaned_data['role']
        user.set_password(self.cleaned_data['password1'])
        user.username = self.cleaned_data['email']  # Use o email como username

        if commit:
            user.save()
        return user