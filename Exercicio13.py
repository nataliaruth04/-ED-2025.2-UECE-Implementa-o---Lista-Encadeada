"""
Exercício 13.
Encontrar o penúltimo nó de uma lista simplesmente encadeada.
A ideia é caminhar pela lista até que o nó seguinte seja o último.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, limite=5):
        self._head = None
        self._size = 0
        self._limite = limite

    def is_empty(self):
        return self._head is None

    def add(self, valor):
        # adiciona no final (estilo lista encadeada padrão)
        if self._size >= self._limite:
            raise ValueError(f"A lista só permite até {self._limite} elementos.")

        novo = Node(valor)

        if self.is_empty():
            self._head = novo
        else:
            atual = self._head
            while atual.next is not None:  # vai até o último
                atual = atual.next
            atual.next = novo

        self._size += 1

    def size(self):
        return self._size

    def __str__(self):
        if self.is_empty():
            return "[]"

        elementos = []
        atual = self._head
        while atual:
            elementos.append(str(atual.data))
            atual = atual.next

        return "[" + " -> ".join(elementos) + "]"


def penultimo_no(lista):
    """
    Retorna o valor do penúltimo nó.
    A lógica é bem direta: enquanto o próximo do próximo nó existir,
    significa que ainda não chegamos no penúltimo.
    """
    if lista._head is None:
        raise ValueError("A lista está vazia.")

    if lista._head.next is None:
        raise ValueError("A lista só tem um elemento, não existe penúltimo.")

    atual = lista._head

    # para quando 'atual.next' for o último (ou seja, next.next == None)
    while atual.next.next is not None:
        atual = atual.next

    return atual.data


# --- Programa principal ---
if __name__ == "__main__":
    lista = LinkedList(limite=5)

    print("Insira até 5 números para montar a lista.")
    while lista.size() < 5:
        entrada = input(f"Valor {lista.size()+1}: ").strip()

        if entrada == "":
            break

        try:
            numero = int(entrada)
            lista.add(numero)
            print("Lista atual:", lista)
        except ValueError as e:
            print("Erro:", e)

    print("\nLista final:", lista)

    try:
        valor_penultimo = penultimo_no(lista)
        print("Penúltimo nó:", valor_penultimo)
    except ValueError as e:
        print("Erro:", e)
