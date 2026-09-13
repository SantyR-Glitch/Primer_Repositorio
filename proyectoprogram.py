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

# Una funcion def para el carro electrico

# Una funcion def para el carro de gas

# Una funcion def para la bici 

opcion = int(input("Bienvenido, ¿Que quieres calcular? 1) Carro electrico, 2) Carro de gasolina, 3) Bicicleta, 4) Las 3 opciones: "))

if opcion == 1:

    print(".............................................................")
    print("Aqui se calcula el carro electrico.")
    print(".............................................................")

# Aqui habra la opcion de calcular las emisiones,consumo y la eficiencia de un carro electrico usando una funcion def

elif opcion == 2:

    print(".............................................................")
    print("Aqui se calcula el carro de gasolina.")
    print(".............................................................")

# Aqui habra la opcion de calcular las emisiones,consumo y la eficicia del carro de gas usando una funcion def

elif opcion == 3:

    print(".............................................................")
    print("Aqui se calcula la bicicleta.")
    print(".............................................................")

# Aqui habra la opcion de calcular las emisiones,consumo y la eficiencia de la bicicleta usando una funcion def

elif opcion == 4:

    print(".............................................................")
    print("Aqui se calcularan las 3 opciones")
    print(".............................................................")

    Dc = float(input("¿Cual es la distancia total del trayecto en carro (km)?: "))
    Db = float(input("¿Cual es la distancia recorrida en bicicleta (km)?: "))
    Rg = float(input("¿Cual es el rendimiento del vehiculo a gasolina (km/L)?: "))
    Ae = float(input("¿Cual es el consumo promedio del auto electrico (kWh/km)?: "))
    Cc = float(input("¿Cuantas kcal se gastaron al usar la bicicleta?: "))
    print(".............................................................")

    if Dc <= 0 or Db <= 0 or Rg <= 0 or Ae <= 0 or Cc <= 0:
        print("Los valores deben ser mayores a cero.")
    else:
        resultados = conversion_energia(Dc, Rg, Ae, Cc, Db)
        B, G, E, emision_bicicleta, CO2, CO2_E, eficiencia_gas, eficiencia_electrico, eficiencia_bicicleta = resultados

        print(".............................................................")
        print(f"El consumo de gasolina es: {G:.3f} L")
        print(f"El consumo de electricidad es: {E:.3f} kWh")
        print(f"El gasto especifico de la bicicleta es: {B:.3f} kWh")
        print(f"Las emisiones de CO2 son: {CO2:.3f} kg")
        print(f"Las emisiones de CO2 del auto electrico son: {CO2_E:.3f} kg")
        print(f"La eficiencia del auto a gasolina es: {eficiencia_gas:.3f} kWh/km")
        print(f"La eficiencia del auto electrico es: {eficiencia_electrico:.3f} kWh/km")
        print(f"La eficiencia de la bicicleta es: {eficiencia_bicicleta:.3f} kWh/km")
        print(".............................................................")
else:
    print("No tenemos esa opcion, asi que elige otra del 1 al 4.")

# Añadi formato para que solo se muestren 3 deciamles al dar el resultado