# Estrutura de nó duplamente encadeado
class DNode:
    def __init__(self, dado):
        self.data = dado
        self.prev = None
        self.next = None


# Lista duplamente encadeada com sentinelas
class DoublyLinkedList:
    def __init__(self):
        # sentinelas ajudam a evitar muitos ifs
        self._header = DNode(None)
        self._trailer = DNode(None)
        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def add(self, valor):
        # insere sempre no final
        novo = DNode(valor)
        ultimo = self._trailer.prev

        ultimo.next = novo
        novo.prev = ultimo
        novo.next = self._trailer
        self._trailer.prev = novo

        self._size += 1

    def __len__(self):
        return self._size

    def __str__(self):
        if self.is_empty():
            return "[]"
        items = []
        atual = self._header.next
        while atual != self._trailer:
            items.append(str(atual.data))
            atual = atual.next
        return "[{}]".format(" <-> ".join(items))


# Remove nós duplicados sem alterar a ordem dos elementos
def remover_duplicatas(lista):
    if lista.is_empty():
        return

    vistos = set()
    atual = lista._header.next

    while atual != lista._trailer:
        if atual.data in vistos:
            # remover o nó da lista
            anterior = atual.prev
            proximo = atual.next
            anterior.next = proximo
            proximo.prev = anterior
            lista._size -= 1

            atual = proximo  # continuar avançando
        else:
            vistos.add(atual.data)
            atual = atual.next


# ------------ PROGRAMA PRINCIPAL --------------

print("=" * 60)
print("REMOVENDO DUPLICATAS EM LISTA DUPLAMENTE ENCADEADA")
print("=" * 60)

while True:
    entrada = input("\nDigite valores separados por espaço (ou 'sair'): ").strip()

    if entrada.lower() == "sair":
        print("Encerrando...")
        break

    lista = DoublyLinkedList()

    # preenchendo lista
    if entrada:
        for item in entrada.split():
            try:
                lista.add(int(item))
            except:
                lista.add(item)

    print(f"\nLista original: {lista}  (tamanho: {len(lista)})")

    remover_duplicatas(lista)

    print(f"Após remover duplicatas: {lista}  (tamanho: {len(lista)})")
    print("-" * 60)
