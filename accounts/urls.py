from django.urls import path, include
from .views import PasswordReset, ProfileView, UpdateProfileView, UserLogin, CreateUserView, LogoutView, PasswordReset, PasswordResetDone, PasswordResetConfirm, PasswordResetCompleteView, PasswordChange
from .api.viewsets import UserProfileViewSet, UsuarioViewSet                 
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')
router.register(r'profile', UserProfileViewSet, basename='profile')


from django.urls import path, include
from .views import PasswordReset, ProfileView, UpdateProfileView, UserLogin, EmocaoDeleteView, CreateUserView, LogoutView, PasswordReset, PasswordResetDone, PasswordResetConfirm, PasswordResetCompleteView, PasswordChange
from .api.viewsets import UserProfileViewSet, UsuarioViewSet                 
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')
router.register(r'profile', UserProfileViewSet, basename='profile')

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('cadastrar/', CreateUserView.as_view(), name='cadastrar'),
    path('entrar/', UserLogin.as_view(), name='entrar'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('perfil/', ProfileView.as_view(), name='perfil'),
    path('excluir_emocao/<int:pk>/', EmocaoDeleteView.as_view(), name='emocao_delete'),
    path('editar-perfil/', UpdateProfileView.as_view(), name='editar-perfil'),
    path('password-reset/', PasswordReset.as_view(), name='password-reset'),
    path('password_reset/done/', PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_complete'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', PasswordChange.as_view(), name='password-change'),
    path('', include(router.urls)),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)