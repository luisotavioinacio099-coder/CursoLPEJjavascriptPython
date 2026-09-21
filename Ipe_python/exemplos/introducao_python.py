# OPERADORES EM PYTHON:
# + --- SOMA
# - --- SUBTRAÇÃO
# * --- MULTIPLICAÇAO
# / --- DIVISÃO
# // DIVIDIR INTEIRA
# % --- MODÚLO(MOD)
# ** --- PONTENCIAÇÃO
# == --- IGUAL A 
# != --- DIFERENTE DE
# > --- MAIOR QUE
# < MENOR QUE
# >= --- MAIOR OU IGUAL A
# <= --- MENOR OU IGUAL A 

#ORDEM DE PRECEDÊNCIA DOS OPERADORES
# 1º Psênteses
# 2º Potenciação
# 3º Multiplicação / Divisão
# 4º Soma/ Suv=btração
# 5º Esquerda para direita

#CASTING: Processo de conversão de dados em Python.
# IMPRIMINDO VALOR:
print('Olá mundo!')

a = 10
b = 5
c = 11

# TRÊS VARIÁVEIS DE TIPO INTEIRO COM MESMO VALOR:
x = y = z = 0

# x = 7
# y = 9
x = int(input('Digite um NÚMERO:'))
y = int(input('Digite outro NÚMERO:'))

z = x + y
print('A SOMA DOS DOIS VALORES É: ',z)

# COMPARANDO DADOS: =================
a = 5
b = 5

# a == b --> true
# b == 6 --> false
# b == a --> true
# b != a + 1 --> true
# a * 2 >= b --> true
# 
#  CONCATENAR COM VIRCULA (,): Junta dados de tipos diferenets.
#  CONCATENAR COM ADIÇÃO (+): JUNTA APENAS DADOS DE TIPOS STRING


print('Digite um NÚMERO: ')
n1 = int(input())
n2 = int(input('Digite outro NÚMERO: '))

a = n1 == n2
print('São iguais? ', n2, '? ', c, '\n')

c = n1 == n2
print(n1, 'é MAIOR que ', n2, '? ', c, '\n')

b= n1 != n2
print('São DIFERENTES? ' + str(b))

#VARIÁVEIS EM PYTHON:
nome = 'Alisson Rocha'
print (nome)

#VARIÁVEIS DO TIPO FLUTUANTE:
n1 = n2 = n3 = n4 = 0.0

#ASSOCIAÇÃO DE VARIÁVEIS:
nome, idade = 'Alisson', 33
media = 12

#VARIÁVEIS BOOLEANO (TRUE/FALSE):
estado_bool = True

# FUNÇÃO TYPE():
print(type(media))
print(type(n2))
print(type(nome))
print(type(estado_bool))
print(type(1+2j))

# FUNÇÃO ISINSTANCE():
a = 10
b = 'Sol'
print(isinstance(a, int))
print(isinstance(a, float))
print(isinstance(a, (int, float)))

#CALCULOS:
a = 40
c = 3
r = a * c
print(r)