import time

from os import system

def limpiar_pantalla():
    system("cls")

limpiar_pantalla()
Validar = True

escenario = [[j + 10 * i + 1 for j in range(10)] for i in range(10)]


asientos = {}
conta = 0
contb = 0
contc = 0


def mostrar_asientos():
    print("A continuacion, se encuentran disponibles los siguientes asientos: ")
    for i in range(10):
        for j in range(10):
            num_asiento = escenario[i][j]
            if num_asiento in asientos:
                print("X\t", end="")
            else:
                print(f"{num_asiento}\t", end="")
            if num_asiento == 100:
                time.sleep(3)
                input("\nPresione (ENTER) si desea continuar ")
                break
        print()


def Comprar_entradas():
    mostrar_asientos()
    cant= int(input("Ingrese la cantidad de entradas a comprar (maximo 3 y minimo 1 por persona) : "))
    if cant <1 and cant >3 : 
        print ("Error, debe ingresar maximo 3 entradas y minimo 1 entrada por persona")
        time.sleep(2)
        limpiar_pantalla()
    asiento = int(input("Ingrese el numero del asiento que desea comprar: "))
    if asiento < 1 or asiento > 100:
        print("Error, el numero de asiento ingresado no es valido ")
        time.sleep(2)
        limpiar_pantalla()
    elif asiento in asientos:
        print("Lo lamentamos, el numero de asiento no esta disponible")
        time.sleep(2)
        limpiar_pantalla()
    else:
        while True:
            run = input("Ingrese el Run (sin guion - ni punto) de la persona que ocupara el asiento para mayor seguridad - FORMATO (123456789): ")
            run = run.replace(".", "").replace("-", "")  
            if len(run) not in (8, 9):
                print("Error, el run ingresado no es valido, debe contener 8 o 9 digitos")
                time.sleep(2)
                limpiar_pantalla()
            else:
                if run.isdigit() or (run[:-1].isdigit() and run[-1].upper() == "K"):
                    break
                else:
                    print("Error, el Run ingresado no es valido")
                    time.sleep(2)
                    limpiar_pantalla()
       
        if asiento <= 20:
            valor = "Platinum"
            precio = 120000
            conta = conta + 1
        elif asiento <= 50 and asiento >=21:
            valor = "Gold"
            precio = 80000
            contb = contb + 1
        else:
            valor = "Silver"
            precio = 50000
            contc = contc + 1
        asientos[asiento] = (run, valor, precio)
        print("¡ Asiento reservado correctamente !")
        time.sleep(3)


def mostrar_ubicaciones_disp():
    mostrar_asientos()


def ver_list_asis():
    print("A continuacion, se mostrara el listado de asistentes:")
    for asiento, datos in sorted(asientos.items(), key=lambda x: x[1][0]):
        run, _valor, _precio = datos
        print(f"{run}: Asiento {asiento}")
        time.sleep(3)
   


def ganancias_totales():
    total = sum(asientos[asiento][2] for asiento in asientos)
    print ("-------TIPO ENTRADA-------CANTIDAD-------TOTAL")
    print (f"Platinum $120.000  ------{conta}")
    print (f"Gold $80.000       ------{contb}")
    print (f"Silver $50.000     -------{contc}")
    print(f"Ganancias totales: ${total}")
    time.sleep(3)


while Validar == True:
    time.sleep(2)
    limpiar_pantalla()
    print("------------ MENU -------------")
    print("1) Comprar entradas")
    print("2) Mostrar ubicaciones disponibles")
    print("3) Ver listado de asistentes")
    print("4) Mostrar ganancias totales")
    print("5) Salir")

    opc = input("Ingrese una opcion: ")

    if opc == "1":
        limpiar_pantalla()
        Comprar_entradas()
    elif opc == "2":
        limpiar_pantalla()
        mostrar_ubicaciones_disp()
    elif opc == "3":
        limpiar_pantalla()
        ver_list_asis()
    elif opc == "4":
        limpiar_pantalla()
        ganancias_totales()
    elif opc == "5":
        Validar = False
        print("*************** ¡ HASTA PRONTO ! Mi nombre es : Javiera Villablanca y hoy estamos a 10 de Julio del año 2023:D ****************")
        time.sleep(3)
    else:
        print("Error, debe ingresar una opcion valida, (1-5)")
