Dc= int(input("¿Cual es la distancia total del trayecto en carro en (km)?:"))
Db= int(input("¿Cual es la distancia recorrida en bicicleta en (km)?:"))
Pu = int(input("¿Cual es tu peso en (kg)?:"))
Rg = int(input("¿Cual es el rendimiento del vehículo a gasolina (km/L)?:"))
Ae = int(input("¿Cual es el consumo promedio del auto eléctrico (kWh/km)?:"))
Cc = int(input("¿Cuantas kcal fueron al usar la bicicleta?:"))

def conversion_energia(Dc, Rg, Ae, Cc, Db):
    litros_gasolina = Dc / Rg
    energia_gasolina = litros_gasolina * 8.9
    emisiones_co2_gasolina = litros_gasolina * 2.31
    energia_auto_electrico = Dc * Ae
    emisiones_co2_auto_electrico = energia_auto_electrico * 0.45
    energia_bicicleta = Cc * 0.001163
    emision_bicicleta = energia_bicicleta * 0.0

    eficiencia_energia_kWh_entre_km_auto_gas = energia_gasolina / Dc
    eficiencia_energia_kWh_entre_km_auto_electrico = Ae
    eficiencia_energia_kWh_entre_km_bicicleta = energia_bicicleta / Db

    return energia_bicicleta, energia_gasolina, energia_auto_electrico, emision_bicicleta, emisiones_co2_gasolina, emisiones_co2_auto_electrico, eficiencia_energia_kWh_entre_km_auto_gas, eficiencia_energia_kWh_entre_km_auto_electrico, eficiencia_energia_kWh_entre_km_bicicleta

if Dc <= 0 or Db <= 0 or Pu <= 0 or Rg <= 0 or Ae <= 0 or Cc <= 0:
    print("Los valores deben ser mayores a cero, por favor ingrese valores válidos.")
else:
    B, G, E, emision_bicicleta, CO2, CO2_E, eficiencia_energia_kWh_entre_km_auto_gas, eficiencia_energia_kWh_entre_km_auto_electrico, eficiencia_energia_kWh_entre_km_bicicleta = conversion_energia(Dc, Rg, Ae, Cc, Db)
    print("El consumo de gasolina es: ", G, "L")
    print("El consumo de electricidad es: ", E, "kWh")
    print("El gasto específico de la bicicleta es: ", B, "kWh")
    print("Las emisiones de CO2 son: ", CO2, "kg")
    print("Las emisiones de CO2 del auto eléctrico son: ", CO2_E, "kg")

    print("La eficiencia de energía del auto a gasolina es: ", eficiencia_energia_kWh_entre_km_auto_gas, "kWh/km")
    print("La eficiencia de energía del auto eléctrico es: ", eficiencia_energia_kWh_entre_km_auto_electrico, "kWh/km")
    print("La eficiencia de energía de la bicicleta es: ", eficiencia_energia_kWh_entre_km_bicicleta, "kWh/km")

int(print("Gracias por usar el programa, hasta luego!"))