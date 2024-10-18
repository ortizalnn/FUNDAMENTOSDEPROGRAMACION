'''
un alumno desea saver cual es su calificacion final
en la materia de algoritmos dicha calificacion
se compone de los siguientes porcentajes:
55% del porcentaje de sus 3 calificaciones parciales.
30% de la calificacion del examen final.
15% de la calificacion de un trabajo final.
entradas: 
c1:
c2:
c3:
examenB:
trabajoF:
salidas:
promedio finalPF:
'''
n1 = int(input("escriba el valor 1: "))
n2 = int(input("escriba el valor 2: "))
n3 = int(input("escriba el valor 3: "))
ef = int(input("escriba el valor EF: "))
tf = int(input("escriba el valor TF: "))
pf = ( n1 + n2 + n3 ) / 3
pf2 = ( pf * 55 / 100 )
ef = ( ef * 30 / 100)
tf = ( tf * 15 / 100 )
pf = ( pf2 + ef + tf )
print("el promedio final es: ",pf)