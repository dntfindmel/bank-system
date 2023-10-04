<div align="center">
<img width="50%" src="https://www.gsan.com.br/lib/exe/fetch.php?cache=&w=900&h=380&tok=2421df&media=ajuda:python-logo.png">
</div>

# Sistema Bancário - PT-BR 🟢🟡
### Feito com Python Orientado a Objetos

Este projeto foi feito para fins de estudo para Python Orientado a Objetos. Foi criado um sistema bancário com três classes:

* Main
* Client
* BankAccount

Dentro da classe **Main** importamos as classes Client e BankAccount de seus respectivos arquivos e passamos alguns valores para os objetos presentes nela. Com a variável `c1 = Client("Melyssa", 11993022296)` passamos o valor para ob objetos _name_ e _phone_ e com a variável `account = BankAccount(c1.get_name(), 1222)` estamos definindo o nome utilizado na variável c1 como o _nome do titular da conta_ e o _1222 como o número da conta_. Em seguida simulamos uma operação bancária de depósito `account.deposit200)`, saque `account.withdrawal(50)` e extrato `account.statement()`, onde o resultado será:

```
Bank Account Owner:  Melyssa 
Current Balance:  150.0
```

Já na classe **Client** definimos no método construtor que nosso objeto terá nome e telefone, que são os dados utilizados para o titular. Como em uma situação real, os dados do titular estão protegidos e não é ideal que sejam acessados de forma direta, para isso criamos as funções `get_name()` feito para ler e retornar o valor de **name** e o `set_name()` que é utilizado para definir um valor para name, sem modificar de forma direta o objeto. **APESAR DE TER FEITO PARA DEMONSTRAR QUE É POSSÍVEL, ESTA NÃO É UMA BOA PRÁTICA PARA UTILIZAR GETTER E SETTER**

O jeito que está na classe **BankAccount** é o mais indicado. Dentro desta classe, passamos os atributos principais _owner_ e _number_ para nosso objeto. Como o valor destes atributos também estão protegidos, novamente devemos usar as propriedades get e set, porém desta vez as escrevendo da forma correta.

```
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
```

O @property é o get e o setter precisa que passemos qual atributo será modificado ou definido. 

Dentro do **BankAccount** também adicionamos mais algumas funções e utilizamos mais dois atributos, o **withdrawal** que é o saque e o **deposit** que é o depósito, ambos utilizam o **amount** que é a quantia que será ou retirada ou colocada e por fim o **statement** que é o nosso extrato.

É um projeto simples, mas muito útil para o treino de Python Orientado a Objetos, já que vemos as classes, os métodos, o método construtor, proteção de atributos e etc. . . Espero que tenham gostado ! <img width="25px" src="https://i.pinimg.com/originals/c9/b2/ed/c9b2edcb9a4d3ca9f0fc01c52f567795.gif">

# Bank System - EN 🔴🔵⚪
### Made with Object Oriented Python

This project was made for study purposes for Object Oriented. A banking system with three classes was created:

* Main
* Client
* BankAccount

Inside the **Main** class we import the Client and BankAccount classes from their respective files and pass some values ​​to the objects present. With the variable `c1 = Client("Melyssa", 11993022296)` we pass the value to the objects _name_ and _phone_ and with the variable `account = BankAccount(c1.get_name(), 1222)` we are defining the name used in the variable c1 as the _account holder name_ and _1222 as the account number_. Next, we simulate a banking operation involving deposit `account.deposit200)`, withdrawal `account.withdrawal(50)` and statement `account.statement()`, where the result will be:

```
Bank Account Owner:  Melyssa 
Current Balance:  150.0
```

In the **Client** class, we define in the constructor method that our object will have a name and a telephone number, which are the data used for the owner. As in a real situation, the holder's data is protected and it's not ideal for it to be accessed directly, for this we created the functions `get_name()` designed to read and return the value of **name** and `set_name ()` which is used to define a value for name, without directly modifying the object. **ALTHOUGH I HAVE DONE TO DEMONSTRATE THAT IT IS POSSIBLE, THIS IS NOT A GOOD PRACTICE FOR USING GETTER AND SETTER**

How I made in **BankAccount** class is the best option. Inside this class, we pass the main attributes _owner_ and _number_ to our object. As the value of these attributes are also protected, we must again use the get and set properties, but this time writing them correctly.

```
    @property
    # Instead of using the name get in the function, we use the property _@property_ which has the same functionality
    def balance(self):
        return self._balance

    @balance.setter
    # The same as above, but with the property set or setter
    def balance(self, balance):
        if balance < 0:
            print("The balance can't be below zero.")
        else:
            self._balance = balance
```

The @property is the get and the .setter needs us to pass which attribute will be modified or set.

Inside **BankAccount** we also added some more functions and used two more attributes, **withdrawal** which is the withdrawal and **deposit** which is the deposit, both use the **amount** which is the amount that will be either withdrawn or placed and finally the **statement** which is our statement.

It's a simple project, but very useful for training Object Oriented Python, as we see classes, methods, the constructor method, attribute protection, etc. . . I hope you guys enjoyed ! <img width="25px" src="https://i.pinimg.com/originals/c9/b2/ed/c9b2edcb9a4d3ca9f0fc01c52f567795.gif">