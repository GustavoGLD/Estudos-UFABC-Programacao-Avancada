"""
Escreva um programa que utilize uma pilha para verificar se expressões aritméticas possuem a parentização correta.
O programa deve garantir que cada parêntese de abertura tenha um parêntese de fechamento correspondente.

Exemplos:
✅ Correto: "(())", "((()()))", "()()"
❌ Incorreto: ")(", "(()(", "))(("
"""
from collections import deque


def check(text: str) -> bool:
    queue = deque[str]()

    for i in range(len(text)):
        letra = text[i]
        letra_anterior = queue[-1] if queue else None

        if letra == '(':
            queue.append(letra)
        elif letra == ')' and (not letra_anterior or letra_anterior != '('):
            return False
        elif letra == ')' and letra_anterior == '(':
            queue.pop()
    else:
        if not queue:
            return True
        else:
            return False


assert check("(())")
assert check("((()()))")
assert check("()()")
assert not check(")(")
assert not check("(()(")
assert not check("))((")
