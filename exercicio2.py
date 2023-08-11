'''
    Crie uma função chamada calcular_area_retangulo que aceite dois parâmetros: 
    base e altura, ambos com valores padrão iguais a 1. A função deve retornar a área 
    do retângulo
'''

def calcular_area_retangulo(base: float = 1, altura: float = 1):
    area = base * altura
    return area

base = float(input("Informe a base do retângulo: "))
altura = float(input("Informe a altura do retângulo: "))
print(f"A área desse retângulo é de {calcular_area_retangulo(base, altura)}")
