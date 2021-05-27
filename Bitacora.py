from datetime import datetime, date, time, timedelta
import calendar

"""Menu"""
def menu():
    print("1- Ingresar una nueva entrada a la bitacora")
    print("2- Ver tu bitacora")
    print("3- Salir del programa")
    op="0"
    while op not in ["1","2","3"]:
        op = input("ingrese opcion deseada")
        if op == "1":
            pass
        if op == "2":
            pass
        if op == "3":
            pass
        if op not in ["1","2","3"]:
            print("Esta opcion no existe")


"""Programa principal"""
menu()
