""" Construir un algoritmo tal, que dado como dato la calificación de un alumno
en un examen, escriba

DEFINICIÓN DEL PROBLEMA
El mismo enunciado.

ANÁLISIS DEL PROBLEMA

Salidas: mensaje de aprobado si se cumple la condición.
Entradas: calificación
Datos adicionales:   un alumno aprueba si la calificación es mayor o igual que 7. """

class Tarea:

   def __init__(self):
       pass
       
   def NFinal(self):
        NT = float(input("Ingrese su Nota final:  "))
        if NT >= 7:
            print("Su nota final es: {}, Felicidades usted ha aprobado el curso ".format(NT))   
        else:
            print("Lo sentimos usted ha Reprobado el Curso, con la siguiente nota {}".format(NT))
               
ejem= Tarea() 
ejem.NFinal()  