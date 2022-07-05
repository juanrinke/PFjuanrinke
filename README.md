# PFjuanrinke

Este es el archivo readme del proyecto.

El proyecto cuenta con las seguientes secciones una vez ingresado:

    path("", views.inicio,),
    path("login", views.login_request , name='Login'),
    path("register", views.register , name='Register'),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path("editarPerfil" , views.editarPerfil , name="editarPerfil"),
    path("about", views.aboutme, name="about")
    path("contacto" , views.contacto),

    path("alta_profesores" , views.alta_profesores ),
    path("profesores" , views.profesores , name="profesores"),
    
    path("cursos" , views.cursos , name="cursos"),
    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path("editar_curso/<int:id>" , views.editar , name="editar_curso"),
    path("editar_curso/" , views.editar , name="editar_curso"),
    path("alta_curso" , views.curso_formulario),
    path("buscar_curso" , views.buscar_curso),
   
    
    path("alumnos" , views.alumnos , name="alumnos" ),
    path("alta_alumnos" , views.alta_alumnos),
    
  
   
   
   asi las organizaria. tengo la sensacion de que se romperia todo si lo intento jaja. Saludos, profe
    
   
