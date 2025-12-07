# Exercício 12
# Implementação das estruturas encadeadas:
# - LinkedStack
# - LinkedQueue
# - CircularQueue
# - LinkedDeque

class Node:
    def __init__(self, dado):
        self.data = dado
        self.next = None


# -----------------------------
#      PILHA ENCADEADA
# -----------------------------
class LinkedStack:
    def __init__(self):
        # topo da pilha (último elemento inserido)
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, item):
        # insere no começo da lista (mais rápido)
        novo = Node(item)
        novo.next = self._head
        self._head = novo
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop em pilha vazia")
        valor = self._head.data
        self._head = self._head.next
        self._size -= 1
        return valor

    def top(self):
        if self.is_empty():
            raise IndexError("top em pilha vazia")
        return self._head.data

    def __str__(self):
        atual = self._head
        itens = []
        while atual:
            itens.append(str(atual.data))
            atual = atual.next
        itens.reverse()
        return f"LinkedStack: [{', '.join(itens)}] <- topo"


# -----------------------------
#        FILA ENCADEADA
# -----------------------------
class LinkedQueue:
    def __init__(self):
        # precisamos manter head (frente) e tail (final)
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, item):
        novo = Node(item)
        if self.is_empty():
            self._head = novo
        else:
            self._tail.next = novo
        self._tail = novo
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue em fila vazia")
        valor = self._head.data
        self._head = self._head.next
        self._size -= 1
        if self.is_empty():   # se esvaziou, tail também vira None
            self._tail = None
        return valor

    def first(self):
        if self.is_empty():
            raise IndexError("first em fila vazia")
        return self._head.data

    def __str__(self):
        atual = self._head
        itens = []
        while atual:
            itens.append(str(atual.data))
            atual = atual.next
        return f"LinkedQueue: [{', '.join(itens)}]"


# -----------------------------
#        FILA CIRCULAR
# -----------------------------
class CircularQueue:
    def __init__(self):
        self._tail = None   # tail aponta para o último, cujo next é o primeiro
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, item):
        novo = Node(item)
        if self.is_empty():
            novo.next = novo
            self._tail = novo
        else:
            novo.next = self._tail.next
            self._tail.next = novo
            self._tail = novo
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue em fila circular vazia")
        head = self._tail.next
        valor = head.data

        if self._size == 1:
            self._tail = None
        else:
            self._tail.next = head.next

        self._size -= 1
        return valor

    def first(self):
        if self.is_empty():
            raise IndexError("first em fila circular vazia")
        return self._tail.next.data

    def rotate(self):
        # só move o tail para o próximo
        if not self.is_empty():
            self._tail = self._tail.next

    def __str__(self):
        if self.is_empty():
            return "CircularQueue: []"
        atual = self._tail.next
        itens = []
        for _ in range(self._size):
            itens.append(str(atual.data))
            atual = atual.next
        return f"CircularQueue: [{', '.join(itens)}]"


# -----------------------------
#           DEQUE
# -----------------------------
# nó duplo para o deque
class DNode:
    def __init__(self, dado):
        self.data = dado
        self.prev = None
        self.next = None


class LinkedDeque:
    def __init__(self):
        # uso de sentinelas para facilitar remoções
        self._header = DNode(None)
        self._trailer = DNode(None)

        self._header.next = self._trailer
        self._trailer.prev = self._header

        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _add_between(self, item, anterior, proximo):
        # insere item entre dois nós
        novo = DNode(item)
        novo.prev = anterior
        novo.next = proximo
        anterior.next = novo
        proximo.prev = novo
        self._size += 1

    def _delete_node(self, node):
        ant = node.prev
        prox = node.next
        ant.next = prox
        prox.prev = ant
        self._size -= 1
        return node.data

    def add_first(self, item):
        self._add_between(item, self._header, self._header.next)

    def add_last(self, item):
        self._add_between(item, self._trailer.prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise IndexError("delete_first em deque vazio")
        return self._delete_node(self._header.next)

    def delete_last(self):
        if self.is_empty():
            raise IndexError("delete_last em deque vazio")
        return self._delete_node(self._trailer.prev)

    def first(self):
        if self.is_empty():
            raise IndexError("first em deque vazio")
        return self._header.next.data

    def last(self):
        if self.is_empty():
            raise IndexError("last em deque vazio")
        return self._trailer.prev.data

    def __str__(self):
        itens = []
        atual = self._header.next
        while atual != self._trailer:
            itens.append(str(atual.data))
            atual = atual.next
        return f"LinkedDeque: [{', '.join(itens)}]"


# ----------------------------------------------
# só para ver funcionando
# ----------------------------------------------
if __name__ == "__main__":
    print("Testando estruturas do Exercício 12:\n")

    # pilha
    P = LinkedStack()
    P.push(10)
    P.push(20)
    P.push(30)
    print(P)
    print("pop:", P.pop(), "\n")

    # fila
    Q = LinkedQueue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    print(Q)
    print("dequeue:", Q.dequeue(), "\n")

    # fila circular
    CQ = CircularQueue()
    CQ.enqueue("A")
    CQ.enqueue("B")
    CQ.enqueue("C")
    print(CQ)
    CQ.rotate()
    print("depois do rotate:", CQ)
    print("dequeue:", CQ.dequeue(), "\n")

    # deque
    D = LinkedDeque()
    D.add_first(9)
    D.add_last(15)
    D.add_first(3)
    print(D)
    print("delete_last:", D.delete_last())
    print("delete_first:", D.delete_first())
    print(D)
