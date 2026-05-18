#Creamos la clase ATM
class Atm:
  # Construimos nuestro constructor para incializar atributos
  def __init__(self,pin):
    #Self hace referencia a la instancia del objeto actual
    # para private "__", para protect "_"
    self.__pin = pin #private #pin siempre va a ser el primer valor que debe contener nuestra clase y es privada
    self._balance = 1000 #protect este atributo e

  # Agregamos metodos

  # tendra parametros self para referencia a la instancia y amount cantidad que recibe
  def deposit(self, amount):
    self._balance += amount
    print("deposito exitoso. Saldo actual: ", self._balance)

  def withdraw(self, amount):
    if amount <= self._balance:
      self._balance -= amount
      print("Retiro relaizado correctamente", self._balance)
    else:
      print("Saldo insuficiente. saldo actual: ", self._balance)
    
  def show_balance(self):
    print("Tu saldo actual es: [ ", self._balance, " ]")

  #Ahora un metodo para cambiar pin, pero este es privado porque lo declaramo arriba al inicio de este archivo
  def change_pin(self,new_pin): #Private
    if self.__pin != new_pin:
      self.__set_pin(new_pin)
      print("PIN modificado correctamente")
    else:
      print("El pin debe ser diferente al nuevo, estas usando el mismo pin")
  
  def validate_pin(self, pin):
    return self.__pin == pin

  # Metodo para cambiar pin
  def __set_pin(self,new_pin): #private
    self.__pin = new_pin