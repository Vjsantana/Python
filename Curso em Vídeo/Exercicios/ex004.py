algo = input('Digite algo:')
print('O tipo primitivo desse valor é {}:' .format(type(algo)))
print('Só tem espaços?', algo.isspace())
print('É um número?', algo.isnumeric())
print('É alfabético?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())
print('Está em letras maiúsculas?', algo.isupper())
print('Está em letras minúsculas?', algo.islower())
print('Está capitalizada?', algo.istitle())

"""No caso da opção de apresentar o tipo da variável digitada acima, o 'type' sempre será uma string pois
a funçao 'input' retorna sempre uma string. Além do mais, não foi especificado, antes da função input, 
o tipo da variável que desejamos que o programa retorne."""
