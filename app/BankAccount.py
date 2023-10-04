class BankAccount:
    # O metódo init é um método construtor necessário para passarmos os parâmetros do nosso objeto
    def __init__(self, owner, number):
        self._balance = 0.0
        self._number = number
        self._owner = owner

    @property
    # Ao invés de usarmos o nome get na função, utilizamos a propriedade property que tem a mesma funcionalidade
    def balance(self):
        return self._balance

    @balance.setter
    # O mesmo caso acima, mas com a propriedade set ou setter
    def balance(self, balance):
        if balance < 0:
            print("The balance can't be below zero.")
        else:
            self._balance = balance

    # Função withdrawal (saque) que recebe os atributos self (ele mesmo) e o amount (valor)
    def withdrawal(self, amount):
        # Se self.balance (o objeto balance - saldo) for maior ou igual ao valor do saque
        if self.balance >= amount:
            # Irá ser retirador do balance - saldo o valor indicado
            self.balance -= amount
            print("Cash withdrawal made sucessfully!")
        else:
            # Caso o primeiro if for falso, irá aparecer a mensagem de saldo insuficiente
            print("Insufficient balance.")

    # A função depósito que tem como atributo ela mesma e o valor acrescenta o valor indicado em seu saldo
    def deposit(self, amount):
        self.balance += amount

    # A função extrato que tem como atributo ela mesma imprime o nome do titular e seu saldo
    def statement(self):
        print("Bank Account Owner: ", self._owner, "\nCurrent Balance: ", self._balance)
