#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el
#4% de interés al año. Estos ahorros debido a intereses, que no se cobran
#hasta finales de año, se te añaden al balance final de tu cuenta de ahorros.
#Escribir un programa que comience leyendo la cantidad de dinero depositada
#en la cuenta de ahorros, introducida por el usuario. Después el programa debe
#calcular y mostrar por pantalla la cantidad de ahorros tras el primer,
#segundo y tercer años. Redondear cada cantidad a dos decimales.
deposito_inicial = float(input("Introduce la cantidad de dinero depositada: "))
# Definir la tasa de interés anual
interes_anual = 0.04
# Calcular el saldo después de cada año
saldo_anio_1 = deposito_inicial * (1 + interes_anual)
saldo_anio_2 = saldo_anio_1 * (1 + interes_anual)
saldo_anio_3 = saldo_anio_2 * (1 + interes_anual)
# Mostrar los resultados redondeados a dos decimales
print(f"Ahorros después del primer año: {saldo_anio_1:.2f}")
print(f"Ahorros después del segundo año: {saldo_anio_2:.2f}")
print(f"Ahorros después del tercer año: {saldo_anio_3:.2f}")