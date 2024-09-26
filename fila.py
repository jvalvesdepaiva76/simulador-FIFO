from processo import Processo
class FilaException(Exception):
    """Classe de exceção lançada quando uma violação de acesso aos elementos da fila é identificada."""
    def __init__(self, msg):
        super().__init__(msg)


class No:
    def __init__(self, carga: any):
        self.__carga = carga
        self.__prox = None


    @property
    def carga(self) -> any:
        return self.__carga


    @property
    def prox(self) -> 'No':
        return self.__prox


    @carga.setter
    def carga(self, novaCarga: any):
        self.__carga = novaCarga


    @prox.setter
    def prox(self, novoProx: 'No'):
        self.__prox = novoProx


    def __str__(self):
        return f'{self.__carga}'




class Head:
    """Classe que representa o nó cabeça (controle) da fila encadeada."""
    def __init__(self):
        self.inicio = None  # Apontador para o primeiro nó
        self.fim = None     # Apontador para o último nó
        self.tamanho = 0    # Tamanho da fila


class Fila:
    """Classe que implementa a estrutura de dados Fila utilizando encadeamento com nó cabeça."""
    def __init__(self):
        self.__head = Head()


    def estaVazia(self) -> bool:
        return self.__head.tamanho == 0


    def __len__(self) -> int:
        return self.__head.tamanho


    def enfileirar(self, carga: any):
        """Adiciona um novo elemento ao final da fila."""
        novo = No(carga)
        if self.estaVazia():
            self.__head.inicio = self.__head.fim = novo
        else:
            self.__head.fim.prox = novo
            self.__head.fim = novo
        self.__head.tamanho += 1


    def desenfileirar(self) -> any:
        """Remove e retorna o elemento da frente da fila."""
        if self.estaVazia():
            raise FilaException(f'A fila está vazia! Não é possível remover elementos.')
       
        carga = self.__head.inicio.carga


        if self.__head.tamanho == 1:
            self.__head.fim = None


        self.__head.inicio = self.__head.inicio.prox
        self.__head.tamanho -= 1
        return carga


    def elementoDaFrente(self) -> any:
        """Retorna o conteúdo armazenado no elemento da frente da fila, sem removê-lo."""
        if self.estaVazia():
            raise FilaException(f'Fila Vazia. Não há elemento a recuperar.')
        return self.__head.inicio.carga


    def __str__(self):
        """Retorna uma string representando os elementos na fila."""
        s = 'frente->[ '
        cursor = self.__head.inicio
        while cursor is not None:
            s += f'{cursor.carga}, '
            cursor = cursor.prox
        return s[:-2] + " ]" if not self.estaVazia() else s + ' ]'
