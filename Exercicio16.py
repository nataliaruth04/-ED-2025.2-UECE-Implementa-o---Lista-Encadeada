"""
Exercício 16.
Implemente uma função que conta o número de nós em uma lista
circularmente encadeada.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self._tail = None   # a lista circular guarda só o tail

    def is_empty(self):
        return self._tail is None

    def add(self, item):
        novo = Node(item)

        # caso especial: lista vazia
        if self.is_empty():
            novo.next = novo       # aponta pra ele mesmo
            self._tail = novo
        else:
            # inserindo depois do tail (que aponta para o "primeiro")
            novo.next = self._tail.next
            self._tail.next = novo
            self._tail = novo      # agora o novo vira o tail

    def __str__(self):
        if self.is_empty():
            return "[]"

        itens = []
        atual = self._tail.next    # começo da lista
        inicio = atual

        while True:
            itens.append(str(atual.data))
            atual = atual.next
            if atual == inicio:
                break

        return f"[{' -> '.join(itens)} -> (circular)]"


def contar_nos(lista):
    """Conta quantos nós existem percorrendo até voltar ao início."""
    if lista._tail is None:
        return 0

    # começa no "head", que é tail.next
    atual = lista._tail.next
    qtd = 1   # já começamos contando o primeiro

    # anda até reencontrar o mesmo nó
    while atual.next != lista._tail.next:
        qtd += 1
        atual = atual.next

    return qtd


# Demonstração
print("=" * 60)
print("CONTAGEM DE NÓS EM LISTA CIRCULAR")
print("=" * 60)

while True:
    entrada = input("\nDigite valores separados por espaço (ou 'sair'): ")

    if entrada.lower() == "sair":
        print("Encerrando...")
        break

    lista = CircularLinkedList()

    if entrada.strip():
        for valor in entrada.split():
            try:
                lista.add(int(valor))
            except:
                lista.add(valor)

    print(f"Lista circular: {lista}")
    total = contar_nos(lista)
    print(f"Total de nós: {total}")
    print("-" * 60)
