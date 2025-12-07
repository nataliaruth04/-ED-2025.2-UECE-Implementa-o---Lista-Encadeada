# Exercício 20:
# Implementar um método reverse que inverta a lista duplamente encadeada

class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedBase:
    def __init__(self):
        # usando header e trailer como nós sentinelas
        self._header = DNode(None)
        self._trailer = DNode(None)
        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def _insert_between(self, item, a, b):
        novo = DNode(item)
        novo.prev = a
        novo.next = b
        a.next = novo
        b.prev = novo
        self._size += 1
        return novo

    def _delete_node(self, node):
        anterior = node.prev
        proximo = node.next
        anterior.next = proximo
        proximo.prev = anterior
        self._size -= 1
        valor = node.data
        node.prev = node.next = None
        return valor

    def add_first(self, item):
        self._insert_between(item, self._header, self._header.next)

    def add_last(self, item):
        self._insert_between(item, self._trailer.prev, self._trailer)

    def reverse(self):
        # percorrer a lista e trocar next <-> prev de cada nó
        atual = self._header
        
        # caminhando por toda a estrutura, incluindo sentinelas
        while atual is not None:
            antigo_prox = atual.next
            atual.next = atual.prev
            atual.prev = antigo_prox
            atual = antigo_prox
        
        # depois da inversão, header e trailer trocam de função
        self._header, self._trailer = self._trailer, self._header

    def __str__(self):
        if self.is_empty():
            return "[]"
        itens = []
        cursor = self._header.next
        while cursor != self._trailer:
            itens.append(str(cursor.data))
            cursor = cursor.next
        return f"[{' <-> '.join(itens)}]"


print("=" * 60)
print("TESTE DO MÉTODO reverse EM LISTA DUPLAMENTE ENCADEADA")
print("=" * 60)

while True:
    entrada = input("\nDigite valores (separados por espaço) ou 'sair':\n→ ")

    if entrada.lower() == "sair":
        print("Encerrando...")
        break

    lista = DoublyLinkedBase()

    if entrada.strip():
        for valor in entrada.split():
            try:
                lista.add_last(int(valor))
            except:
                lista.add_last(valor)

    if lista.is_empty():
        print("Lista vazia, nada para inverter.")
        continue

    print(f"\nLista original: {lista}")
    lista.reverse()
    print(f"Lista invertida: {lista}")
    print("-" * 60)
