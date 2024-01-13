from django import forms 

class ContatoForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)
    
class ReservaForm(forms.Form):
    nome_pet = forms.CharField(label='Nome do Pet')
    telefone = forms.CharField(label='Telefone')
    dia_reserva = forms.DateField(label='Dia da Reserva')
    observacoes = forms.CharField(label='Observações', widget=forms.Textarea)