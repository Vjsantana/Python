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
"""O resultado exibido será: <class 'int'>
Veja a seguir mais um exemplo com outro tipo de variável"""

print(type(divisao))

#cCONVERSÃO DE UMA VARIÁVEL

"""Para convertermos uma variável de um tipo qualquer para o tipo string, por exemplo, basta acrescentarmos 
as iniciais 'str' no início da variável. Veja um exemplo abaixo:"""

print('Soma: '+ str(soma))
"""O resultado exibido será: 'soma: 15' 
Vamos agora converter a variável 'divisao' que está no tipo float para o tipo int."""

print(int(divisao))
"""O resultado será '2' ao invés de '2.0' conforme apresentado na mesma operação feita anteriormente, 
quando o tipo da variável 'divisao' era float"""

#MÉTODO '.FORMAT'

"""É utilizado para concatenar strings e variáveis sem a necessidade de realizar conversões. Veja 
um exemplo abaixo"""

print('soma: {} ' .format(soma))

"""As chaves '{}' são utilizadas para substituir a variável que desejamos concatenar quando utilizamos 
o método '.format'. Podemos incluir mais de uma variável na mesma linha. Veja o exemplo a seguir"""

print('soma: {} e subtração: {} ' .format(soma, subtracao))

"""Outra forma de escrevermos o código acima é: """

print('soma: {soma} e subtração: {subtracao} ' .format(soma=soma, subtracao=subtracao))

"""Note que se incluírmos o nome da variável dentro das chaves precisaremos indentificá-la após o método 
'.format' """

#QUEBRA DE LINHA NO PYTHON

"""Para incluírmos uma quebra de linha no código """




