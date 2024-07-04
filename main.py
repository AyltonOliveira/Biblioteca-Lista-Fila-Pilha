import ListaDuplamenteEncadeada
import Fila
import Pilha

# Classe que representa um livro com título, autor e código.
class Livro:
    def __init__(self, titulo, autor, codigo):
        self.codigo = codigo
        self.autor = autor
        self.titulo = titulo

# Classe que gerencia o catálogo de livros.
class Catalogo:
    def __init__(self):
        self.catalogo = ListaDuplamenteEncadeada.DoublyLinkedListIterator()

    # Método para adicionar um livro ao catálogo.
    def addLivro(self, titulo, autor, codigo):
        livro = Livro(titulo, autor, codigo)
        self.catalogo.addNode(livro)

    # Método para imprimir todos os livros do catálogo.
    def print_catalogo(self):
        self.catalogo.print_list()

    # Método para buscar um livro pelo título no catálogo.
    def buscarLivro(self, titulo):
        current = self.catalogo.firstNode
        while current is not None:
            if current.data.titulo == titulo:
                return current.data
            current = current.nextNode
        return None

# Classe que gerencia os empréstimos de livros.
class Emprestimo:
    def __init__(self):
        self.pilha = Pilha.ArrayStack()

    # Método para realizar um empréstimo de livro.
    def emprestimo(self, livro):
        self.pilha.push(livro)

    # Método para devolver um livro.
    def devolucao(self):
        return self.pilha.pop()

# Classe que gerencia a fila de espera para reserva de livros.
class FilaEspera:
    def __init__(self):
        self.fila = Fila.ArrayQueue()

    # Método para reservar um livro.
    def reservar(self, livro):
        self.fila.enqueue(livro)

    # Método para cancelar uma reserva.
    def cancelarReserva(self):
        return self.fila.dequeue()

# Classe que representa a interface do usuário.
class UserInterface:
    def __init__(self):
        self.catalogo = Catalogo()
        self.emprestimo = Emprestimo()
        self.filaEspera = FilaEspera()

    # Método que exibe o menu principal.
    def mainMenu(self):
        while True:
            try:
                # Exibe as opções do menu para o usuário.
                print("\nOla, digite o que deseja fazer!")
                print("1: Adicionar livro")
                print("2: Buscar livro")
                print("3: Solicitar empréstimo")
                print("4: Entrar na fila de espera")
                print("5: Devolver livro")
                print("0: Sair")
                men = int(input("Escolha uma opção: "))
            except ValueError:
                print("Por favor, digite um número válido de 0 a 5.")
                continue

            # Adicionar um livro ao catálogo.
            if men == 1:
                titulo = input("Digite o título do livro: ")
                autor = input("Digite o autor do livro: ")
                codigo = input("Digite o código do livro: ")
                self.catalogo.addLivro(titulo, autor, codigo)
                print(f"Livro '{titulo}' adicionado com sucesso!")
            # Buscar um livro no catálogo.
            elif men == 2:
                titulo = input("Digite o título do livro: ")
                livro = self.catalogo.buscarLivro(titulo)
                if livro:
                    print(f"O livro '{livro.titulo}' está disponível no catálogo.")
                else:
                    print("Livro não encontrado no catálogo.")
            # Solicitar um empréstimo de livro.
            elif men == 3:
                titulo = input("Digite o título do livro para empréstimo: ")
                livro = self.catalogo.buscarLivro(titulo)
                if livro:
                    self.emprestimo.emprestimo(livro)
                    print(f"'{livro.titulo}' emprestado com sucesso.")
                else:
                    print("Livro indisponível.")
            # Entrar na fila de espera para um livro.
            elif men == 4:
                titulo = input("Digite o título do livro para reserva: ")
                livro = self.catalogo.buscarLivro(titulo)
                if livro:
                    self.filaEspera.reservar(livro)
                    print(f"'{livro.titulo}' adicionado à fila de espera.")
                else:
                    print("Livro indisponível.")
            # Devolver um livro.
            elif men == 5:
                livro_devolvido = self.emprestimo.devolucao()
                if livro_devolvido:
                    print(f"'{livro_devolvido.titulo}' devolvido com sucesso.")
                else:
                    print("Não há livros para devolver.")
            # Sair do programa.
            elif men == 0:
                print("Saindo do sistema. Até logo!")
                break

# Execução do programa principal.
if __name__ == "__main__":
    ui = UserInterface()
    ui.mainMenu()
