from typing import Generic, TypeVar, Optional, List

T = TypeVar("T")

class ArrayStack(Generic[T]):
    """Pilha implementada com um array que cresce e encolhe quando precisa.
    Ideia básica: último a entrar é o primeiro a sair (LIFO)."""

    _MIN_CAPACITY = 8

    def __init__(self, capacity: int = 10) -> None:
        # Cria o array interno com um tamanho inicial mínimo.
        self._buf: List[Optional[T]] = [None] * max(capacity, self._MIN_CAPACITY)
        self._n = 0  # quantidade de elementos guardados

    def __len__(self) -> int:
        return self._n

    def is_empty(self) -> bool:
        return self._n == 0

    def push(self, value: T) -> None:
        # Se não tiver espaço, dobramos o tamanho do array.
        if self._n == len(self._buf):
            self._grow(len(self._buf) * 2)
        self._buf[self._n] = value
        self._n += 1

    def pop(self) -> T:
        # Só dá pra tirar se a pilha não estiver vazia.
        if self.is_empty():
            raise IndexError("pop de pilha vazia")

        self._n -= 1
        val = self._buf[self._n]
        self._buf[self._n] = None  # limpa a posição
        # Encolhe se estiver ocupando pouco espaço.
        if len(self._buf) > self._MIN_CAPACITY and self._n < len(self._buf) // 4:
            self._shrink(max(len(self._buf) // 2, self._MIN_CAPACITY))

        return val  # type: ignore

    def top(self) -> T:
        # Olha o topo sem remover nada.
        if self.is_empty():
            raise IndexError("top de pilha vazia")
        return self._buf[self._n - 1]  # type: ignore

    def _grow(self, new_cap: int) -> None:
        # Copia tudo para um array maior.
        novo = [None] * new_cap
        for i in range(self._n):
            novo[i] = self._buf[i]
        self._buf = novo

    def _shrink(self, new_cap: int) -> None:
        # Mesma ideia do grow, só que reduzindo.
        novo = [None] * new_cap
        for i in range(self._n):
            novo[i] = self._buf[i]
        self._buf = novo

    def __repr__(self) -> str:
        conteudo = ", ".join(repr(self._buf[i]) for i in range(self._n))
        return f"ArrayStack([{conteudo}]) <- topo"


class ArrayQueue(Generic[T]):
    """Fila usando buffer circular.
    A regra aqui é: o primeiro que entra é o primeiro que sai (FIFO)."""

    _MIN_CAPACITY = 8

    def __init__(self, capacity: int = 10) -> None:
        # Cria o vetor circular.
        self._buf: List[Optional[T]] = [None] * max(capacity, self._MIN_CAPACITY)
        self._head = 0   # posição do primeiro elemento
        self._count = 0  # quantidade total

    def __len__(self) -> int:
        return self._count

    def is_empty(self) -> bool:
        return self._count == 0

    def enqueue(self, value: T) -> None:
        # Se encheu, redimensiona.
        if self._count == len(self._buf):
            self._resize(len(self._buf) * 2)

        tail = (self._head + self._count) % len(self._buf)
        self._buf[tail] = value
        self._count += 1

    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError("dequeue de fila vazia")

        val = self._buf[self._head]
        self._buf[self._head] = None
        self._head = (self._head + 1) % len(self._buf)
        self._count -= 1

        # Se estiver usando pouco, reduz o array.
        if len(self._buf) > self._MIN_CAPACITY and self._count < len(self._buf) // 4:
            self._resize(max(len(self._buf) // 2, self._MIN_CAPACITY))

        return val  # type: ignore

    def first(self) -> T:
        if self.is_empty():
            raise IndexError("first de fila vazia")
        return self._buf[self._head]  # type: ignore

    def _resize(self, new_cap: int) -> None:
        # Copia os elementos na ordem certa pra um vetor novo.
        novo = [None] * new_cap
        for i in range(self._count):
            novo[i] = self._buf[(self._head + i) % len(self._buf)]
        self._buf = novo
        self._head = 0

    def __repr__(self) -> str:
        itens = [repr(self._buf[(self._head + i) % len(self._buf)]) for i in range(self._count)]
        return f"ArrayQueue([{', '.join(itens)}]) <- rear"


class ArrayDeque(Generic[T]):
    """Deque (fila de duas pontas) usando array circular.
    Dá pra inserir e remover tanto no começo quanto no fim."""

    _MIN_CAPACITY = 8

    def __init__(self, capacity: int = 10) -> None:
        self._buf: List[Optional[T]] = [None] * max(capacity, self._MIN_CAPACITY)
        self._start = 0  # índice do primeiro elemento
        self._len = 0    # quantidade de elementos

    def __len__(self) -> int:
        return self._len

    def is_empty(self) -> bool:
        return self._len == 0

    def add_first(self, value: T) -> None:
        # Se estiver cheio, aumenta primeiro.
        if self._len == len(self._buf):
            self._resize(len(self._buf) * 2)

        # Move o início para trás no círculo.
        self._start = (self._start - 1) % len(self._buf)
        self._buf[self._start] = value
        self._len += 1

    def add_last(self, value: T) -> None:
        if self._len == len(self._buf):
            self._resize(len(self._buf) * 2)

        tail = (self._start + self._len) % len(self._buf)
        self._buf[tail] = value
        self._len += 1

    def delete_first(self) -> T:
        if self.is_empty():
            raise IndexError("delete_first de deque vazio")

        val = self._buf[self._start]
        self._buf[self._start] = None
        self._start = (self._start + 1) % len(self._buf)
        self._len -= 1

        # Reduz se estiver muito folgado.
        if len(self._buf) > self._MIN_CAPACITY and self._len < len(self._buf) // 4:
            self._resize(max(len(self._buf) // 2, self._MIN_CAPACITY))

        return val  # type: ignore

    def delete_last(self) -> T:
        if self.is_empty():
            raise IndexError("delete_last de deque vazio")

        tail = (self._start + self._len - 1) % len(self._buf)
        val = self._buf[tail]
        self._buf[tail] = None
        self._len -= 1

        if len(self._buf) > self._MIN_CAPACITY and self._len < len(self._buf) // 4:
            self._resize(max(len(self._buf) // 2, self._MIN_CAPACITY))

        return val  # type: ignore

    def first(self) -> T:
        if self.is_empty():
            raise IndexError("first de deque vazio")
        return self._buf[self._start]  # type: ignore

    def last(self) -> T:
        if self.is_empty():
            raise IndexError("last de deque vazio")
        tail = (self._start + self._len - 1) % len(self._buf)
        return self._buf[tail]  # type: ignore

    def _resize(self, new_cap: int) -> None:
        # Realinha tudo no início do novo array.
        novo = [None] * new_cap
        for i in range(self._len):
            novo[i] = self._buf[(self._start + i) % len(self._buf)]
        self._buf = novo
        self._start = 0

    def __repr__(self) -> str:
        itens = [repr(self._buf[(self._start + i) % len(self._buf)]) for i in range(self._len)]
        return f"ArrayDeque([{', '.join(itens)}])"
