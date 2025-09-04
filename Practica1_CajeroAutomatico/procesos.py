def consultar(saldo) :
    print("Su actual es: $", saldo)

def depositar(saldo) :
   dp = int(input("Ingrese la cantidad a depositar: $"))
   saldo += dp
   print("Deposito exitoso!")
   return saldo

def retirar(saldo) :
    rt = int(input("Ingrese la cantidad a retirar: "))
    if rt <= saldo :
        saldo -= rt
        print("Retiro exitoso!")
    elif rt > saldo :
        print("No hay saldo suficiente")
    return saldo 



def menu(saldo) :
    entrar = True
    while entrar :
        print("Bienvenido Cajero ATM ")
        print("1. Consultar Saldo ")
        print("2. Depositar saldo ")
        print("3. Retirar Saldo ")
        print("4. Salir del Cajero ")
        op = int(input("Opcion: "))

        if op == 1 :
            consultar(saldo)
        elif op == 2 :
            saldo = depositar(saldo)
        elif op == 3 :
            saldo = retirar(saldo)
        elif op == 4 :
            exit()
        else :
            print("Opcion invalida...")
