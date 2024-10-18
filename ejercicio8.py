'''
un vendedor resive un sueldo base, mas un 10% extra por comicion de sus ventas
, el vendedor desea saber cuanto dinero obtendra por concepto de comiciones
por las tres ventas que realiza en el mes y el total que recibira en el mes 
tomando en cuenta su sueldo base y comiciones.
entrada:
saldob:
valor1:
valor2:
valor3:
totalC:
salidas:
sueldoT:
'''
sb = input("escribe el sueldo base: ")
sb = int(sb)
v1 = input("escribe el valor 1: ")
v1 = int(v1)
v2 = input("escribe el valor 2: ")
v2 = int(v2)
v3 = input("escribe el valor 3: ")
v3 = int(v3)
tc = input("escribe el total de comiciones: ")
tc = int(tc)
ct = ( sb + v1 + v2 + v3 ) * 10
st = ( sb + ct )
print("el sueldo total es: ", st)