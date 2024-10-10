'''
Programa que calcule el area y el perimetro 
de unrectangulo a partir de su base y su altura
Entradas
base: Integer
altura: integer
salida:
perimetro: integer
area: interger
Analisis:
Se requiere calcular con las formulas para 
area y perimetro
'''
#input siempre regresa un string
# para tratarlo como otro dato se debe convertir
base = input("Escribe la base del rectangulo: ")
base = int (base)
altura = imput("Escribe la altura del rectangulo")
altura = int(altura)
area = base * altura
primetro = base + base + altura + altura
primetro = (base + altura) + 2
print(area)
print(perimetro)