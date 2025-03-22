from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(
        '<h1 style="color:red">Hello, world. You\'re at the dashboard index.</h1>'
    )
    # ^ Retorna uma resposta HTTP com HTML embutido, estilizando o texto diretamente com CSS inline.


def staff(request):
    # O Django sempre passa um objeto HttpRequest como primeiro argumento para as views,
    # mesmo que ele não seja utilizado, garantindo compatibilidade com o framework.
    return HttpResponse("Hello, world. You're at the dashboard staff.")


# def index(request):
#     return render(request, 'dashboard/index.html')
