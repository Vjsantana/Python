n1 = int(input('Digite o primeiro número'))
n2 = int(input('Digite o segundo número'))
soma = n1 + n2
print('A soma dos números é:', soma)
print('A soma entre', n1, 'e', n2, 'vale:', (soma))

# O comando 'print' acima pode ser escrito de forma mais simples utilizando o comando '.format'. Veja:

print('A soma entre {} e {} totaliza:{}'.format(n1, n2, soma))
