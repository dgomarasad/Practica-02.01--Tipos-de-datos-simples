#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día
#tiene un descuento del 60%. Escribir un programa que comience leyendo el
#número de barras vendidas que no son del día. Después el programa debe
#mostrar el precio habitual de una barra de pan, el descuento que se le
#hace por no ser fresca y la ganancia final total.
# Definir constantes
PRECIO_BARRA = 3.49
DESCUENTO = 0.60

barras_no_frescas = int(input("Barras de pan no frescas vendidas: "))

descuento_por_barra = PRECIO_BARRA * DESCUENTO
precio_barra_descuento = PRECIO_BARRA - descuento_por_barra

ganancia_total = barras_no_frescas * precio_barra_descuento

print(f"Precio habitual de una barra de pan: {PRECIO_BARRA:.2f}€")
print(f"Descuento por no ser fresca: {descuento_por_barra:.2f}€")
print(f"Ganancia total por vender {barras_no_frescas} barras no frescas: {ganancia_total:.2f}€")