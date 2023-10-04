# Foi criado uma classe com o nome Client para armazenar o código do nosso objeto
class Client:
    # O metódo init é um método construtor necessário para passarmos os parâmetros do nosso objeto
    def __init__(self, n, phone):
        self._name = n
        self._telephone = phone

    # get_name é um getter para retornar o valor de name respeitando sya proteção
    def get_name(self):
        return self._name

    # set_name é um setter para ler e definir o valor de name sem mudar o objeto de forma direta
    def set_name(self, name):
        self._name = name
