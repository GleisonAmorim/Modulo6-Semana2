from django.shortcuts import render
from .forms import ContatoForm, ReservaForm

def inicio(request):
    return render(request, 'inicio.html')

def contato(request):
    sucesso = False
    if request.method == 'GET':
        form = ContatoForm()
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            sucesso = True
    resposta = {
        'telefone': '(16) 9999-9999',
        'responsavel': 'Maria Silva',
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'contato.html', resposta)

from django.shortcuts import render
from .forms import ReservaForm

def reserva(request):
    sucesso = False
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            #  adicionar lógica para processar a reserva
            sucesso = True
    else:
        form = ReservaForm()

    resposta = {'form': form, 'sucesso': sucesso}
    return render(request, 'reserva.html', resposta)

