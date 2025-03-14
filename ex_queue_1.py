"""
Considere uma pilha que armazene caracteres.
Faça uma função para determinar se uma string está no formato XY,
onde X é uma cadeia formada por caracteres arbitrários e Y é o reverso de X.
Por exemplo, se X = ABCD, então Y = DCBA. Considere que X e Y são duas strings distintas.
"""

from queue import LifoQueue


def check(texto: str) -> bool:
    if len(texto) % 2 != 0:
        return False

    myqueue = LifoQueue()

    for letra in texto:
        myqueue.put(letra)

    for letra in texto:
        if letra != myqueue.get():
            return False

    return True


print(check("ABCDDCBA"))  # True
print(check("ABCDEDCBA"))  # False
print(check("AABB"))  # False
