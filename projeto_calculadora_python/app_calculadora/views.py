from django.shortcuts import render

# Create your views here.


def calcular_soma(request):
    if request.method == 'POST':
        valor1 = int(request.POST.get('valor1'))
        valor2 = int(request.POST.get('valor2'))
        operacao = request.POST.get('operacao')

        resultado = 'Hello World!'
        
        return render(request, 'calculadora/calculadora.html', {'valor1': valor1, 'valor2': valor2,'resultado': resultado})
    else:
        return render(request, 'calculadora/calculadora.html')