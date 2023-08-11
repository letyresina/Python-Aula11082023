# Parâmetro Default

def calcularMedia(matematica: float = 0, fisica: float = 0, quimica: float = 0): # posso indicar o tipo indicado para determinada variável
    print(f"Matemática: {matematica}")
    print(f"Física: {fisica}")
    print(f"Química: {quimica}")
    media = (matematica + fisica + quimica) / 3
    return media

print(f"Média: {calcularMedia(10, 8, 6)}")

print("\n")

# Parametro nomeado, onde não preciso respeitar a ordem colocada anteriormente, eu chamo na ordem que desejo
print(f"Média {calcularMedia(quimica=10, matematica=8, fisica=9)}")

'''
    Explicação: na parte do código matematica: float = 0, esse = 0 é um parametro default.
    É o valor pré definido que pode ser alterado ou não, caso não colocado, é dado como o valor default
    Chamando a função, eu não preciso obrigatoriamente (nesse caso) passar todos os parametros.
    Posso ter o valor default sem a denotação do tipo como matematica = 0
'''
