a = 10
b = 5

#Para inserir comentários em apenas uma linha no Python basta inciar com o símbolo "#" Hashtag.

"""Para inserir comentários em mais de uma linha no Python digite o seu comentário entre três aspas simples ou 
três aspas duplas. O comentário aparecerá na forma de uma string mas não irá gerar bytecod."""

#OPERADORES ARITMÉTICOS.
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
exponenciacao = a ** b
print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(resto)
print(exponenciacao)

#CONSULTAR O TIPO DE UMA VARIÁVEL

"""Se desejarmos consultar o 'tipo' de uma variável podemos utilizar a palavra 'type'. veja um exemplo abaixo:"""

print(type(soma))
"""O resultado exibido será: <class 'int'>"""

#cCONVERSÃO DE UMA VARIÁVEL

"""Para convertermos uma variável de um tipo qualquer para o tipo string, por exemplo, basta acrescentarmos 
as iniciais 'str' no início da variável. Veja um exemplo abaixo:"""

print('soma: '+ str(soma))
"""O resultado exibido será: 'soma: 15' """




