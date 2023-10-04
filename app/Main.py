# Aqui importamos do arquivo Client a classe Cliente e do arquivo BankAccount a classe BankAccount
from Client import Client
from BankAccount import BankAccount


# Como a classe Main não tem nenhum objeto, utilizamos o pass
class Main:
    pass


# Aqui estamos colocando dentro de uma variável o nome do cliente e seu telefone
c1 = Client("Melyssa", 11993022296)

# Aqui passamos dentro da variável que o nome do titular é o nome do cliente acima e o número de sua conta
account = BankAccount(c1.get_name(), 1222)

# Função para depositar na conta do titular passado na variável account
account.deposit(200)

# Função para sacar na conta do titular passado na variável account
account.withdrawal(50)

# Função para ler o quanto tem de saldo na conta do titular da variável account
account.statement()
