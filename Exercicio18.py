"""
Exercício 18.
A ideia é pegar uma lista encadeada que tem números misturados
(positivos e negativos) e separar esses valores em duas outras listas:
uma só com positivos e outra só com negativos.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        # insere sempre no final da lista
        novo = Node(item)
        if self.is_empty():
            self._head = novo
        else:
            atual = self._head
            while atual.next:
                atual = atual.next
            atual.next = novo

    def __str__(self):
        if self.is_empty():
            return "[]"
        itens = []
        atual = self._head
        while atual:
            itens.append(str(atual.data))
            atual = atual.next
        return "[" + " -> ".join(itens) + "]"


def separar_lista(orig):
    # cria duas listas vazias para armazenar cada grupo
    positivos = LinkedList()
    negativos = LinkedList()

    atual = orig._head
    while atual:
        if atual.data > 0:
            positivos.add(atual.data)
        elif atual.data < 0:
            negativos.add(atual.data)
        # zeros simplesmente não entram em nenhuma lista
        atual = atual.next

    return positivos, negativos


print("=" * 60)
print("SEPARAÇÃO DE POSITIVOS E NEGATIVOS")
print("=" * 60)

while True:
    entrada = input("\nDigite números separados por espaço (ou 'sair'): ")

    if entrada.lower() == "sair":
        print("Encerrando...")
        break

    lista = LinkedList()

    # preenche a lista original
    if entrada.strip():
        for valor in entrada.split():
            try:
                lista.add(int(valor))
            except:
                print(f"Aviso: '{valor}' não é número inteiro, então foi ignorado.")

    if lista.is_empty():
        print("A lista está vazia.")
        continue

    print(f"\nLista original: {lista}")

    positivos, negativos = separar_lista(lista)

    print(f"Positivos: {positivos}")
    print(f"Negativos: {negativos}")
    print("-" * 60)
