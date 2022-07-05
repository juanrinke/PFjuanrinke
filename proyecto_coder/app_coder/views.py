from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso, Alumno, Profesor, Avatar
from django.template import loader
from app_coder.forms import Curso_formulario, Profesor_formulario, Alumno_formulario, UserEditForm
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.   


def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render( request , "padre.html")

@login_required
def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos" : cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )

@login_required
def alta_curso(request, nombre):
    curso = Curso(nombre=nombre , camada=287318)
    curso.save()
    texto = f"Se guardo en la BD el Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(texto)

@login_required
def alumnos(request):

    return render( request , "alumnos.html" )

@login_required
def contacto(request):

    return render( request , "contacto.html" )   

def profesores(request):

    return render( request , "profesores.html" )   


@login_required
def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            curso = Curso( nombre=datos['nombre'] , camada=datos['camada'])
            curso.save()

            return render( request , "formulario.html")

    return render( request, "formulario.html")
@login_required
def alta_profesores(request):

    if request.method == "POST":

        mi_formulario = Profesor_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            profesor = Profesor( nombre=datos['nombre'] , legajo=datos['legajo'])
            profesor.save()

            return render( request , "formulario.html")

    return render( request, "alta_profesores.html")
@login_required
def alta_alumnos(request):

    if request.method == "POST":

        mi_formulario = Alumno_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            alumno = Alumno( nombre=datos['nombre'] , camada=datos['camada'], nacimiento=datos['nacimiento'])
            alumno.save()

            return render( request , "formulario.html")

    return render( request, "alta_alumnos.html")





def buscar_curso(request):

    return render( request , "buscar_curso.html")



def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html" , {"cursos": cursos})
    else:
        return HttpResponse("Campo vacio")
@login_required
def elimina_curso (request, nombre_curso):

    curso = Curso.objects.get(nombre=nombre_curso)
    curso.delete()

    curso = Curso.objects.all()

    return render(request, "cursos.html" , {"cursos": cursos})
@login_required
def editar (request, id):

    curso= Curso.objects.get (id=id)

    if request.method == "POST":

        mi_formulario= Curso_formulario (request.POST)
        if mi_formulario.is_valid():
            datos= mi_formulario.cleaned_data
            curso.nombre=datos-['nombre']
            curso.camada=datos-['camada']
            curso.save()

            curso= Curso.objects.all()
        

            return render(request, "cursos.html" , {"cursos": cursos})
    else:
        mi_formulario = Curso_formulario(initial={'nombre':curso.nombre, "camada": curso.camada })

    return render ( request, "editar_curso.html" , {"mi _formulario":mi_formulario, "curso": curso})


def login_request (request):

    if request.method =="POST":

        form = AuthenticationForm (request , data= request.POST)

        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user =authenticate(username=usuario , password=contra)

            if user is not None:
                login(request, user)
                avatares =Avatar.objects.filter(user=request.user.id)
                return render( request, "inicio.html")

            else:
                return HttpResponse ("Usuario Incorrecto")

        else:
            return HttpResponse (f"Form Incorrecto {form}")


    form = AuthenticationForm()

    return render(request, "login.html", {"form":form})

def register(request):

    if request.method == "POST":
        
        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()
            return HttpResponse("Usuario creado")



    else:
        form=UserCreationForm()
    return render (request, "registro.html" , {"form":form})


@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":

        miFormulario =UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email =informacion ['email']
            password =informacion ['password1']
            usuario.set_password (password)
            usuario.save()

            return render (request, "inicio.html")

        pass

    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
        return render( request, "editar_perfil.html", {"miFormulario":miFormulario,"usuario":usuario})


def aboutme(request):

    return render (request, "about.html")

   