from django.urls import path,reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from apps.usuario import views

app_name = 'usuario'

urlpatterns = [
    path('', LoginView.as_view(template_name='index.html'), name='login'),
    path('inicio', login_required(TemplateView.as_view(template_name='usuario/usuario_index.html')),
         name='inicio_usuario'),
    path('registrar', views.RegistroUsuario.as_view(), name='registrar'),
    path('reset/password_reset',
         PasswordResetView.as_view(template_name='password_reset/password_reset_form.html',
                                   email_template_name='password_reset/password_reset_email.html',
                                   success_url=reverse_lazy('usuario:password_reset_done')),
         name='password_reset'),
    path('password_reset_done',
         PasswordResetDoneView.as_view(template_name='password_reset/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_confirm.html',
                                          success_url=reverse_lazy('usuario:password_reset_complete')),
         name='password_reset_confirm'),
    path('reset/done',
         PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
         name='password_reset_complete'),
]
