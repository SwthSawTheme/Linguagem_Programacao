# Exemplos de tipos de dados em python

# Definição dos tipos
nome = "Saw" # String
idade = 20 # Int
altura = 1.83 # Float
beleza = False # Bool
peso = "80.0" # String

# Saida
print(f"O dado {nome} é da  {type(nome)}")
print(f"O dado {idade} é da  {type(idade)}")
print(f"O dado {altura} é da  {type(altura)}")
print(f"O dado {beleza} é da  {type(beleza)}")
# Peso apesar de guardar um número do tipo float, é uma String!
# Todo e qualquer valor entre aspas simples ou dupla, que não foi convertido
# É uma string!
print(f"O dado {peso} é da  {type(peso)}")