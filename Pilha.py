class ArrayStack: #(Pilha implementada por um array (uma lista))
# atributos, propriedades ou estados

    def __init__(self): #construtor. cria e retorna uma pilha vazia
        self._data = []

    def __len__(self): #retorna quantos elementos estão na pilha
        return len(self._data)
    
    def is_empty(self): #retorna True se a pilha estiver vazia, else False.
        return len(self._data) == 0

    def push(self, e): #adiciona o elemento e no topo da pilha
        self._data.append(e)

    def top(self): #retorna o elemento do topo da pilha, mas não o remove
        if self.is_empty():
            print('pilha vazia')
            return None
        else:
            return self._data[-1]  
        
    def pop(self): #remove e retorna o elemento do topo da pilha
        if self.is_empty():
           # print('Pilha Vazia')
            return None
        else:
            return self._data.pop()