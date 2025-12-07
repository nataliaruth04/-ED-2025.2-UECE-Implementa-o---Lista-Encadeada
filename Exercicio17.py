# Exercício 17
# Algoritmo recursivo para inverter uma lista simplesmente encadeada

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
        # adiciona no final da lista
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


def reverter_recursivo(no):
    # caso base: chegou no final da lista
    if no is None or no.next is None:
        return no
    
    # chama recursivamente até o último nó
    nova_cabeca = reverter_recursivo(no.next)
    
    # inverte a ligação do próximo para o atual
    no.next.next = no
    no.next = None
    
    return nova_cabeca


def reverter(lista):
    # apenas substitui o head pelo que a recursão devolveu
    lista._head = reverter_recursivo(lista._head)


print("=" * 60)
print("REVERSÃO RECURSIVA DE LISTA ENCADEADA")
print("=" * 60)

while True:
    entrada = input("\nDigite valores separados por espaço (ou 'sair'): ")
    
    if entrada.lower() == "sair":
        print("Encerrando...")
        break
    
    lista = LinkedList()
    
    if entrada.strip():
        for valor in entrada.split():
            try:
                lista.add(int(valor))
            except:
                lista.add(valor)
    
    print(f"\nLista original:  {lista}")
    reverter(lista)
    print(f"Lista invertida: {lista}")
    print("-" * 60)
