from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as do_logout, login, authenticate

# Create your views here.
class ContactView(TemplateView):
    template_name='contact.html'
    def get(self, request, *args, **kwargs):
        context = {
            'titulo': 'Contacto y pedidos',
            'form': AuthenticationForm()
        }
        return render(request, self.template_name, context)

class CheckView(TemplateView):
    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # Hacemos el login manualmente
                login(request, user)
                # Y le redireccionamos a la portada
                return redirect('index')
        return redirect('/contacto/')

def logout(request):
    do_logout(request)
    return redirect('index')



