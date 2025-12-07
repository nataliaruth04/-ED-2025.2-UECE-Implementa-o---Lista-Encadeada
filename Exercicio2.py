"""
Exercício 2.
Execute a seguinte série de operações em uma pilha inicialmente vazia:

push(5), push(3), pop(), push(2), push(8), pop(), pop(), push(9), push(1), pop(),
push(7), push(6), pop(), pop(), push(4), pop(), pop().

Neste arquivo eu implementei uma pilha simples (array-based) e simulei a sequência
passo a passo, mostrando o estado após cada operação.
"""

from typing import List, Optional

class SimpleArrayStack:
    """Pilha baseada em array (dinâmico) — versão simples pra fixar a ideia."""
    def __init__(self, capacity: int = 8) -> None:
        # iniciando o buffer com None (capacidade inicial)
        self._buf: List[Optional[int]] = [None] * max(2, capacity)
        self._size = 0  # quantos caras estão na pilha

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def push(self, value: int) -> None:
        # se encheu, dobra a capacidade (manualmente)
        if self._size == len(self._buf):
            self._resize(len(self._buf) * 2)
        # coloca no próximo índice livre (topo lógico)
        self._buf[self._size] = value
        self._size += 1
        # comentário de estudante: empilhei, bora pro próximo!

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("pop em pilha vazia")
        self._size -= 1
        val = self._buf[self._size]
        self._buf[self._size] = None  # limpa (boa prática)
        # se ficou muuuuito vazio, encolhe pra economizar memória
        if len(self._buf) >= 16 and self._size <= len(self._buf) // 4:
            self._resize(len(self._buf) // 2)
        # comentário de estudante: retirei o topo e tá devolvendo o valor
        return val  # type: ignore

    def top(self) -> int:
        if self.is_empty():
            raise IndexError("top em pilha vazia")
        return self._buf[self._size - 1]  # type: ignore

    def _resize(self, new_cap: int) -> None:
        # cria novo buffer e copia elementos (base->topo)
        new_buf: List[Optional[int]] = [None] * max(2, new_cap)
        for i in range(self._size):
            new_buf[i] = self._buf[i]
        self._buf = new_buf
        # comentário de estudante: resize feito, agora com espaço novo

    def to_list(self) -> List[int]:
        """Retorna uma lista com os elementos na ordem base->topo (só pra print)."""
        return [self._buf[i] for i in range(self._size)]  # type: ignore

    def __repr__(self) -> str:
        elems = ", ".join(str(x) for x in self.to_list())
        return f"SimpleArrayStack([{elems}]) <- topo"


# --------------------------
# Simulação da sequência
# --------------------------

OPERATIONS = [
    "push(5)", "push(3)", "pop()", "push(2)", "push(8)",
    "pop()", "pop()", "push(9)", "push(1)", "pop()",
    "push(7)", "push(6)", "pop()", "pop()", "push(4)",
    "pop()", "pop()"
]

def parse_push(op: str) -> Optional[int]:
    """Pegue o valor de um 'push(x)' ou None se não for push."""
    if op.startswith("push(") and op.endswith(")"):
        try:
            return int(op[5:-1])
        except ValueError:
            return None
    return None

def simulate_sequence(ops: List[str]) -> None:
    st = SimpleArrayStack()
    pops = []  # guarda o resultado de cada pop em ordem de ocorrência

    print("=" * 60)
    print("Simulação da sequência de operações (estilo estudante):")
    print("=" * 60)

    for idx, op in enumerate(ops, start=1):
        print(f"\n{idx:02d}. Operação: {op}")

        v = parse_push(op)
        if v is not None:
            # comentário de estudante: tô empilhando esse valor aí
            st.push(v)
            print(f"    → push({v}) feito. (coloquei no topo)")
        else:
            # é pop()
            if op.strip() == "pop()":
                if st.is_empty():
                    print("    → pop() tentou, mas a pilha tava vazia :(")
                else:
                    popped = st.pop()
                    pops.append(popped)
                    print(f"    → pop() retornou: {popped}")
            else:
                print("    → operação desconhecida (pulando)")

        # mostrar estado atual da pilha de forma clara
        if st.is_empty():
            print("    Estado atual: []  (pilha vazia)")
        else:
            print(f"    Estado atual: {st.to_list()} (topo = {st.top()})")
        # comentário de estudante: pronto, próximo passo

    print("\n" + "=" * 60)
    print("Resumo final:")
    print(f"  Estado final da pilha: {st.to_list() if not st.is_empty() else []}")
    print(f"  Pilha vazia? {'sim' if st.is_empty() else 'não'}")
    print(f"  Valores retornados por pop(), na ordem: {pops}")
    print("=" * 60)


if __name__ == "__main__":
    simulate_sequence(OPERATIONS)
