"""
2-) Escribe una clase CuentaBancaria que permita representar la cuenta de un cliente
determinado de un banco. La clase debe incluir un atributo para almacenar el
nombre del titular de la cuenta y otro privado para almacenar el saldo actual.
a) Escribe un constructor que inicialice el saldo a cero y el titular con un valor que se
recibirá como
parámetro.
b) Escribe un método que devuelva el saldo actual.
c) Escribe un método ingresar que reciba una cantidad de dinero e incremente el saldo
en dicha cantidad.
Se deberá comprobar que la cantidad es positiva. En caso contrario, el método
simplemente no hace nada.
d) Escribe un método retirar que reciba una cantidad de dinero y decremente el saldo
en dicha cantidad. Se deberá comprobar que la cantidad es menor o igual al saldo
disponible. En caso contrario, el método mostrará el mensaje ’Saldo insuficiente’ y no
modificará el saldo.
e) Sobrescribe el método _str_ para que devuelva una representación en forma de
string de la cuenta bancaria con el siguiente formato:
Titular: nombre_del_titular
Saldo: saldo_actual
f) Escribe un programa que cree dos cuentas bancarias (con cualquier nombre de
titular arbitrario).
A continuación que ingrese 500e en la primera cuenta y 1000e en la segunda, y
muestre por pantalla el contenido de ambas cuentas. A continuación que retire 200e
de cada una de ellas y vuelva a mostrarlas. Finalmente, que intente retirar 400e de la
primera (comprobar que se muestra el mensaje Saldo insuficiente).
"""
class CuentaBancaria:
    def __init__(self, titular):
        self.titular= titular
        self.__saldo_actual = 0

    def get_saldo_actual(self):
        return self.__saldo_actual
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__saldo_actual += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__saldo_actual:
            self.__saldo_actual -= cantidad
        else:
            print("Saldo insuficiente")

    def __str__(self):
        return f"Titular: {self.titular}\n\
                 Saldo: {self.__saldo_actual:,.2f}"
    

# ----- PROGRAMA ----
cuenta1 = CuentaBancaria("Miriam")
cuenta2 = CuentaBancaria("Jorge")

cuenta1.ingresar(500)
cuenta2.ingresar(1000)

print(cuenta1)
print(cuenta2)

cuenta1.retirar(200)
cuenta2.retirar(200)

print(cuenta1)
print(cuenta2)

cuenta1.retirar(400)


