class Person:
    
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        
    def __str__(self):
        return f"""
        ** Datos de la persona **
        Nombre: {self.name}
        Apellido: {self.last_name}
        """
        
    def getName(self):
        print(f'{self.name} {self.last_name}')
        
class Client(Person): 
    
    def __init__(self, name, last_name, numAccount, balance):
        super().__init__(name, last_name)
        self.numAccount = numAccount
        self.balance = balance
    
    def __str__(self):
        
        return super().__str__()+f"""
        ** Datos de cuenta **
        Numéro de cuenta: {self.numAccount}
        Balance: {self.balance}
        """
        
    def deposit(self, amount, client):
        client.balance += amount
        self.balance -= amount
        print(f'Deposito de {amount} realizado a la cuenta de "{client.name} {client.last_name}"')
        
    def withdraw(self, amount):
        self.balance -= amount
        print(f'Retiro de {amount} realizado')
    
    
def createClient():
    client = Client('Alfredo', 'Jiménez', 210, 10000)
    print(str(client))
    return client

createClient()

def start():
    print('Bienvenido usuario NOMBRE DE USUARIO, por favor, escoja alguna opción a realizar')