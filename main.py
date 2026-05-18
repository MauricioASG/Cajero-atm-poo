from atm import Atm

pin = input("Ingressa tu pin: ")
atm = Atm(pin)


#"Agregamos un menu"
user_input = input(
  """
¿Qué proceso desea realizar?
1.- Cambiar el pin
2.- Depositar dinero
3.- Retirar dinero
4.- Consultar dinero
"""
)

if user_input == "1":
  actual_pin = int(input("Ingresa el Pin actual: "))
  if atm.validate_pin(actual_pin):
    new_pin = int(input("Ingresa el nuevo pin: "))
    atm.change_pin(new_pin)
elif user_input == "2":
  amount = int(input("Ingresa la cantidad a depositar: "))
  atm.deposit(amount)
elif user_input == "3":
  amount = int(input("Ingresa la cantidad a retirar : "))
  atm.withdraw(amount)
elif user_input == "4":
  atm.show_balance()
else:
  print("Gracias por usar este servicio")