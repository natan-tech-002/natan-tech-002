# calculadora

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def potenciacao(a, b):
    return a ** b

def radiciacao(a, b):
    if b == 0:
        return "Erro: índice da raiz não pode ser zero!"
    return a ** (1 / b)