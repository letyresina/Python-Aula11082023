'''
    Crie uma função chamada enviar_email que aceite os parâmetros destinatario, 
    assunto e corpo. O parâmetro assunto deve ter um valor padrão de "Sem assunto". 
    O parâmetro corpo deve ter um valor padrão de uma string vazia. A função deve 
    imprimir as informações formatadas. Inclua uma docstring que explique brevemente 
    o propósito da função.
'''

def enviar_email(destinatario, assunto = "Sem assunto", corpo = ""):
    """
        Essa função tem como objetivo mostrar para o usuário, após ele digitar as informações necessárias para enviar
        um e-mail, o que ele digitou.
    """
    print(f"Destinatário: {destinatario}")
    print(f"Assunto: {assunto}")
    print(f"Corpo do e-mail: {corpo}")
    return destinatario, assunto, corpo


#enviar_email(destinatario="leticiaresina@gmail.com")