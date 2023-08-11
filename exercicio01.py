'''
    Escreva uma função chamada mostrar_informacoes que aceite três parâmetros 
    nomeados: nome, idade e cidade. A função deve imprimir uma mensagem 
    formatada com essas informações.
'''

def mostrar_informacoes(nome = "", idade = "", cidade = ""):
    print(f"Nome do usuário: {nome}")
    print(f"Idade do usuário: {idade}")
    print(f"Cidade do usuário: {cidade}")

nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")
cidade = input("Informe sua cidade: ")

mostrar_informacoes(nome, idade, cidade)