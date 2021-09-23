#INTERAGINDO COM O USUÁRIO

"""Podemos executar alguns comandos a fim de interagir com o usuário. Um desses comandos é o 'INPUT' """

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

"""O 'int' é utilizado acima para indicar que o valor das variáveis que devem ser digitadas e 
operacionalizadas devem ser números inteiros. Se não incluírmos essa informação o programa entenderá 
o valor como uma string e não é possível operacionalizarmos strings diretemante."""

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
potenciacao = a ** b
resto = a % b

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(potenciacao)
print(resto)
