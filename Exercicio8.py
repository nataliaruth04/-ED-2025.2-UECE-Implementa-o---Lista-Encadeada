"""
Exercício 8.
Escreva um programa que verifique se, em uma expressão aritmética dada como string,
os parênteses de abertura e fechamento estão bem formados.
"""

class ArrayStack:
    def __init__(self):
        # usando lista normal como base da pilha
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pilha vazia")
        return self._data.pop()


def verifica_parenteses(expr):
    """Checa se os parênteses de uma expressão estão equilibrados"""
    stack = ArrayStack()

    for ch in expr:
        # quando abre, só empilha
        if ch == "(":
            stack.push(ch)

        # quando fecha, precisa ter um "(" antes
        elif ch == ")":
            if stack.is_empty():
                return False
            stack.pop()

    # se a pilha ficou vazia no fim, está ok
    return stack.is_empty()


# Programa principal
print("=" * 50)
print("VERIFICADOR DE PARÊNTESES")
print("=" * 50)

while True:
    entrada = input("\nDigite uma expressão (ou 'sair' para encerrar): ")

    if entrada.lower() == "sair":
        print("Encerrando...")
        break

    if verifica_parenteses(entrada):
        print("✓ Parênteses corretos!")
    else:
        print("✗ Parênteses incorretos.")

    print("-" * 50)
