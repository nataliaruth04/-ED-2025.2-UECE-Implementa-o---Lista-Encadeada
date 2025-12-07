"""
Exercício 6.
Execute a seguinte sequência de operações de fila, assumindo que ela começa vazia:

enqueue(5), enqueue(3), dequeue(), enqueue(2), enqueue(8), dequeue(), dequeue(),
enqueue(9), enqueue(1), dequeue(), enqueue(7), enqueue(6), dequeue(), dequeue(),
enqueue(4), dequeue(), dequeue().
"""

class ArrayQueue:
    def __init__(self):
        # fila usando lista normal mesmo
        self._data = []
    
    def is_empty(self):
        return len(self._data) == 0
    
    def enqueue(self, item):
        # adiciona no final
        self._data.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("fila vazia")
        # remove o primeiro
        return self._data.pop(0)
    
    def __str__(self):
        if self.is_empty():
            return "[]"
        return f"[{', '.join(map(str, self._data))}] <- traseira"


print("EXECUÇÃO DAS OPERAÇÕES NA FILA\n")

fila = ArrayQueue()
dequeue_resultados = []

operacoes = [
    "enqueue(5)", "enqueue(3)", "dequeue()", "enqueue(2)", "enqueue(8)",
    "dequeue()", "dequeue()", "enqueue(9)", "enqueue(1)", "dequeue()",
    "enqueue(7)", "enqueue(6)", "dequeue()", "dequeue()", "enqueue(4)",
    "dequeue()", "dequeue()"
]

for i, op in enumerate(operacoes, 1):
    if op.startswith("enqueue"):
        valor = int(op.split("(")[1].split(")")[0])
        fila.enqueue(valor)
        print(f"{i:2}. {op:15} -> {fila}")
    
    elif op == "dequeue()":
        removido = fila.dequeue()
        dequeue_resultados.append(removido)
        estado_atual = fila if not fila.is_empty() else "[]"
        print(f"{i:2}. {op:15} -> retorna {removido}, fila: {estado_atual}")

print("\n" + "="*50)
print(f"Estado final da fila: {fila}")
print(f"Valores retornados pelos dequeues: {dequeue_resultados}")
print("="*50)
