
from django.urls import path
from AppNueva import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('cursos/', views.cursos, name="Cursos"),
    path('profesores/', views.profesores),
    path('estudiantes/', views.estudiantes),
    path('entregables/', views.entregables, name="entregables"),
    path('form-con-api/', views.form_con_api, name="FormConApi"),
    path('form-con-api_E/', views.form_con_api_E, name="FormConApi"),
     path('form-con-api_P/', views.form_con_api_P, name="FormConApi"),
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar_Form_Con_Api"),
    ]
