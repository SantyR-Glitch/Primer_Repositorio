# Esta Funcion: def conversion_energia(Dc, Rg, Ae, Cc, Db),calcula la eficienica, 
# energia consumida y las emisiones de CO2.
# de un auto de gasolina uno electrico y una bicicleta.
# La variable litros_gasolina usa las variables Dc y Rg para calcular los litros de, 
# gasolina consumidos para usarlos en la funcion de abajo del calculo de,
# su consumo de Energia y se mutiplica por 8.9,
# para pasarlos a kWh, donde Dc se refiere a la distancia recorrida 
# y Rg al rendimiento de Km/L. 
# Despues se calcula emisones_co2_gasolina que indica en kg cuanto CO2 produce.
# Se usa la variable anteriormente descrita que es litros_gasolina,
# cantidad de litros usados y se multiplica por 2.31 para,
# convertirlo y asi obtener el dato sobre las emisiones de CO2.
# La variable energia_auto_electrico nos indica que tanto se consumio en kWh y 
# usa Dc mutiplicandola por Ae donde es Distancia Recorrida por, 
# el Consumo promedio del auto electrico kWh/km respectivamente.
# La variable emisiones_co2_auto_electrico nos indica las emisones de CO2 del carro electrico,
# en Kg y por eso se mutiplica por 0.45.
# La variable energia_bicicleta indica la energia consumida de la bicicleta que es, 
# Cc que son las kcal quemadas por 0.001163 constante el numero para la energia en kWh.
# La variable emision_bicicleta es para calcular las emsiones de CO2 de la bici, y 
# se hace mediante la variable anterior energia_bicicleta * 0.0 ya que, 
# la bicicleta no genera emisiones de CO2.
# La variable eficiencia_energia_kWh_entre_km_auto_gas se refiere a la eficiencia en kWh/Km,
# para medir que tanto vale la pena, usando energia_gasolina / Dc que son la energia en,
# kWh de carro de gasolina entre la distancia recorrida total.
# La variable eficiencia_energia_kWh_entre_km_auto_electrico se refiere a la eficiencia, 
# en kWh del auto electrico y se usa = Ae porque la variable ya esta en kWh/Km.
# La variable eficiencia_energia_kWh_entre_km_bicicleta se refiere a kWh/Km de la bici,
# donde usa energia_bicicleta / Db que es la energia de la bici ya en kWh y la distancia.


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

    return (energia_bicicleta,energia_gasolina,energia_auto_electrico,emision_bicicleta,emisiones_co2_gasolina,emisiones_co2_auto_electrico,eficiencia_energia_kWh_entre_km_auto_gas,eficiencia_energia_kWh_entre_km_auto_electrico,eficiencia_energia_kWh_entre_km_bicicleta)

# Esta Funcion def calculo_carro_electrico(dc, ae), es para calcular, 
# solo el consumo, emisiones y eficiencia del carro electrico.

def calculo_carro_electrico(dc, ae):
    consumo = dc * ae
    emisiones = consumo * 0.45
    eficiencia = ae
    return consumo, emisiones, eficiencia

# Esta Funcion def calculo_carro_gasolina(dc, rg), es para calcular solo el consumo, 
# emisiones y eficiencia del carro de gasolina

def calculo_carro_gasolina(dc, rg):
    litros = dc / rg
    energia = litros * 8.9
    emisiones = litros * 2.31
    eficiencia = energia / dc
    return litros, energia, emisiones, eficiencia

# Esta Funcion def calculo_bicicleta(cc, db), es para calcular solo el consumo, emisiones y 
# eficiencia de la bicicleta

def calculo_bicicleta(cc, db):
    energia = cc * 0.001163
    emisiones = 0.0
    eficiencia = energia / db
    return energia, emisiones, eficiencia


# Este es el menu de opciones donde el usuario o persona que quiera usar la calculadora,
# ecologica tendra que escoger dentro de las opciones cual quiere uasar del 1 al 4.

opcion = int(input("Bienvenido, ¿Que quieres calcular? 1) Carro electrico, 2) Carro de gasolina, 3) Bicicleta, 4) Las 3 opciones: "))

if opcion == 1:
    print(".............................................................")
    print("Aqui se calcula el carro electrico.")
    print(".............................................................")

    dc = float(input("¿Cual fue la distancia total en carro (km)?: "))
    ae = float(input("¿Cual es el consumo promedio del auto electrico (kWh/km)?: "))

    if dc <= 0 or ae <= 0:
        print("Los valores deben ser mayores a cero.")
    else:
        consumo, emisiones, eficiencia = calculo_carro_electrico(dc, ae)
        print(".............................................................")
        print(f"El consumo de electricidad es: {consumo:.3f} kWh")
        print(f"Las emisiones de CO2 del auto electrico son: {emisiones:.3f} kg")
        print(f"La eficiencia del auto electrico es: {eficiencia:.3f} kWh/km")
        print(".............................................................")

elif opcion == 2:
    print(".............................................................")
    print("Aqui se calcula el carro de gasolina.")
    print(".............................................................")

    dc = float(input("¿Cual fue la distancia total en carro (km)?: "))
    rg = float(input("¿Cual es el rendimiento del carro de gasolina (km/L)?: "))

    if dc <= 0 or rg <= 0:
        print("Los valores deben ser mayores a cero.")
    else:
        litros, energia, emisiones, eficiencia = calculo_carro_gasolina(dc, rg)
        print(".............................................................")
        print(f"El consumo de gasolina es: {litros:.3f} L")
        print(f"La energia consumida es: {energia:.3f} kWh")
        print(f"Las emisiones de CO2 del carro de gasolina son: {emisiones:.3f} kg")
        print(f"La eficiencia del auto de gasolina es: {eficiencia:.3f} kWh/km")
        print(".............................................................")

elif opcion == 3:
    print(".............................................................")
    print("Aqui se calcula la bicicleta.")
    print(".............................................................")

    cc = float(input("¿Cuantas kcal consumiste o quemaste al usar la bicicleta?: "))
    db = float(input("¿Cual es la distancia recorrida en bicicleta (km)?: "))

    if cc <= 0 or db <= 0:
        print("Los valores deben ser mayores a cero.")
    else:
        energia, emisiones, eficiencia = calculo_bicicleta(cc, db)
        print(".............................................................")
        print(f"El gasto especifico de la bicicleta es: {energia:.3f} kWh")
        print(f"Las emisiones de CO2 de la bicicleta son: {emisiones:.3f} kg")
        print(f"La eficiencia de la bicicleta es: {eficiencia:.3f} kWh/km")
        print(".............................................................")

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