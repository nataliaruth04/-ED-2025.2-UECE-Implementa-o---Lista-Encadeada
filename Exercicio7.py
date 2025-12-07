"""
Exercício 7.
Execute a sequência de operações em um deque inicialmente vazio:
add first(4), add last(8), add last(9), add first(5), back(), delete first(), delete last(),
add last(7), first(), last(), add last(6), delete first(), delete first().
"""

class ArrayDeque:
    def __init__(self):
        # usando lista normal para simular o deque
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def add_first(self, item):
        # adiciona no começo (como se fosse a frente do deque)
        self._data.insert(0, item)

    def add_last(self, item):
        # adiciona no final
        self._data.append(item)

    def delete_first(self):
        # remove o primeiro se existir
        if self.is_empty():
            raise IndexError("deque vazio")
        return self._data.pop(0)

    def delete_last(self):
        # remove o último elemento
        if self.is_empty():
            raise IndexError("deque vazio")
        return self._data.pop()

    def first(self):
        if self.is_empty():
            raise IndexError("deque vazio")
        return self._data[0]

    def last(self):
        if self.is_empty():
            raise IndexError("deque vazio")
        return self._data[-1]

    def __str__(self):
        if self.is_empty():
            return "[]"
        return f"[{', '.join(map(str, self._data))}]"


# execução das operações
print("OPERAÇÕES NO DEQUE\n")

dq = ArrayDeque()

ops = [
    "add_first(4)", "add_last(8)", "add_last(9)", "add_first(5)",
    "last()", "delete_first()", "delete_last()", "add_last(7)",
    "first()", "last()", "add_last(6)", "delete_first()", "delete_first()"
]

for i, op in enumerate(ops, 1):
    print(f"{i:2}. {op:18}", end="")

    if "add_first" in op:
        valor = int(op.split("(")[1].split(")")[0])
        dq.add_first(valor)
        print(f" → {dq}")

    elif "add_last" in op:
        valor = int(op.split("(")[1].split(")")[0])
        dq.add_last(valor)
        print(f" → {dq}")

    elif op == "delete_first()":
        removido = dq.delete_first()
        print(f" → remove {removido}, deque: {dq}")

    elif op == "delete_last()":
        removido = dq.delete_last()
        print(f" → remove {removido}, deque: {dq}")

    elif op == "first()":
        retorno = dq.first()
        print(f" → retorna {retorno}")

    elif op == "last()":
        retorno = dq.last()
        print(f" → retorna {retorno}")

print("\n" + "=" * 50)
print(f"Estado final do deque: {dq}")
print("=" * 50)
