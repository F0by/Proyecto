from django.shortcuts import render
from django.http import HttpResponse
from AppNueva.forms import CursoFormulario
from AppNueva.models import Curso
from AppNueva.models import Estudiante
from AppNueva.forms import BuscaCursoForm

def inicio(request):
    return render(request, "AppNueva/index.html")

def cursos(request):
    return render(request, "AppNueva/cursos.html")

def profesores(request):
    return HttpResponse("Vista profesores")

def estudiantes(request):
    return HttpResponse("Vista estudiantes")

def entregables(request):
    return HttpResponse("Vista entregables")

def form_con_api(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()

            return render(request, "AppNueva/index.html")
    else:
        mi_formulario = CursoFormulario()

    return render(request, "AppNueva/form_con_api.html", {"mi_formulario": mi_formulario})

def form_con_api_E(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["mail"])
            estudiante.save()

            return render(request, "AppNueva/index.html")
    else:
        mi_formulario = CursoFormulario()

    return render(request, "AppNueva/form_con_api.html", {"mi_formulario": mi_formulario})




def buscar_form_con_api(request):
    if request.method == "POST":
        mi_formulario = BuscaCursoForm(request.POST) # Aqui me llega la informacion del html

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "AppNueva/mostrar_cursos.html", {"cursos": cursos})
    else:
        mi_formulario = BuscaCursoForm()

    return render(request, "AppNueva/buscar_form_con_api.html", {"mi_formulario": mi_formulario})
