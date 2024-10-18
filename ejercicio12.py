'''
Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos 
puntos en el plano. Calcula y muestra la distancia entre ellos.
entradas:
px1:
py1:
px2:
pY2:
salidas:
d:
'''
px1 = int(input("escribe el valor del punto 1x: "))
py1 = int(input("escribe el valor del punto 1y: "))
px2 = int(input("escribe el valor del punto 2x: "))
py2 = int(input("escribe el valor del punto 2y: "))
d = (px1 - px2) * + (py2 - py1 ) * 1/2
print("la distancia entre ellos es de: ",d)