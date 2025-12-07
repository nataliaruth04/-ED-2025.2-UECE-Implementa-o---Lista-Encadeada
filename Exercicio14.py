# Exercício 14: Concatenar duas listas encadeadas simples

class Node:
    def __init__(self, dado):
        self.dado = dado
        self.next = None


class LinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def is_empty(self):
        return self._head is None

    def add(self, item):
        novo = Node(item)
        if self.is_empty():
            self._head = novo
        else:
            atual = self._head
            while atual.next:
                atual = atual.next
            atual.next = novo
        self._size += 1

    def __len__(self):
        return self._size

    def __str__(self):
        if self.is_empty():
            return "[]"
        itens = []
        aux = self._head
        while aux:
            itens.append(str(aux.dado))
            aux = aux.next
        return "[" + " -> ".join(itens) + "]"


def concatenar(L, M):
    """
    Junta a lista M ao final da lista L.
    Depois da operação, M fica vazia.
    """
    if L.is_empty():
        L._head = M._head
        L._size = M._size
    else:
        atual = L._head
        # anda até o último nó de L
        while atual.next:
            atual = atual.next
        atual.next = M._head
        L._size += M._size

    # esvazia M após a concatenação
    M._head = None
    M._size = 0


# Exemplo de uso
print("=== CONCATENAÇÃO DE LISTAS ===\n")

L = LinkedList()
M = LinkedList()

# preenchendo L
for v in [1, 2, 3]:
    L.add(v)

# preenchendo M
for v in [4, 5, 6]:
    M.add(v)

print("Antes:")
print("L =", L)
print("M =", M)

concatenar(L, M)

print("\nDepois:")
print("L =", L)
print("M =", M)
