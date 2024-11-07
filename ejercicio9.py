''' 
una tienda ofrece un descueto del 15% sobre el total de la
compra y un cliente desea saber cuanto debera pagar 
finalmente por su compra
entrada:
total de compra: = tc
salidas:
total de compra - descuento
precio final: 
'''
tc = input("escribe el total de compra: ")
tc = int(tc)
tc = ( 15 * tc / 100 )
print("el total de la compra es: ",tc)