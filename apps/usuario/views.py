from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from apps.usuario.forms import RegistroForm
from django.urls import reverse_lazy

# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = "registro.html"
    form_class = RegistroForm
    success_url = "/"
