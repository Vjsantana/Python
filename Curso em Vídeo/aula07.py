#ORDEM DE RESOLUÇÃO DOS OPERADORES ARITMÉTICOS
op1a = 5+3*2
print(op1a)

"""O resultado da operação aritmética realizada em 'op1' é 11. Note que o programa respeitou a ordem de 
precedência das operações aritméticas em python, ou seja, ele resolveu primeiro a multiplicação e em 
seguida a adição. Agora note nas operação a seguir, utilizando os mesmos números, como o resultado é 
alterado pela utilização de parênteses. Vejamos:"""

op1b = (5+3)*2
print(op1b)

"""O resultado agora é 16. Isso ocorreu porque os parênteses em python são quem determinam a ordem em que 
uma operação aritmética será realizada. No caso acima, executou-se primeiro a adição e, logo em seguida, 
a multiplicação."""