import procesos as p
saldo = 1000
pin = 1234
intentos = 3

while intentos != 0 :
    pin_user = int(input("Ingrese el pin: "))
    if pin == pin_user :
        p.menu(saldo)
    if pin != pin_user :
        intentos -= 1
    if intentos == 0 :
        print("❌Tarjeta Bloqueada❌")    
