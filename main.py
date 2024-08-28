#
# autor: Michel
# data: 21-08-2024

# importar classes
# from nome_do_arquivo import nome_da_classe as alias
# nome_do_arquivo sem a extensão .py
# alias é um apelido que você dá para a classe
from classevazia import ClasseVazia as CV
from pessoa import Pessoa as P 


# instanciar classes
p1 = P() # p1 é um objeto do tipo Pessoa.
cv1 = CV() # cv1 é um objeto do tipo ClasseVazia.
l1 = list() # l1 é um objeto do tipo list.
p2 = P() # p2 é um objeto do tipo Pessoa.
# p1 e p2 são objetos do tipo Pessoa, mas são objetos diferentes.
# p1 e p2 são instâncias da classe Pessoa.
# p1 e p2 possuem endereços de memória diferentes.
# assim como os demais objetos instanciados.


# 
print(f"p1 -> {p1}") # endereço de memória do objeto p1.
print(f"p2 -> {p2}")

print(f"p1.nome -> {p1.nome}") # acessando o atributo nome do objeto p1.

p1.nome = "Michel" # alterando o valor do atributo nome do objeto p1.

print(f"p1.nome -> {p1.nome}")
p1.nome = "Davi"
print(f"p1.nome -> {p1.nome}")

p1.olaMundo() # chamando o método olaMundo do objeto p1.


