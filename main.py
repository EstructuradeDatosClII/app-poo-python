from model.Persona import Persona
from model.Curso import Curso
#Creando la instancia de Persona en el objeto objPersona
objPersona = Persona("Luis",
                     "Salvatierra",
                     "12304040",
                     "lsalvatierra@gmail.com")

objPersona.saludar()
#Creando la instancia de Curso en el objeto objCurso
objCurso = Curso("C001", "EPOO 1", 5)
objCurso.bienvenido()
objCurso.set_nombre("Base de datos")
objCurso.set_credito(4)
objCurso.bienvenido()