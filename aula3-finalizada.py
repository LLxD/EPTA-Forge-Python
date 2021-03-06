#recap
#variaveis
#operações matemáticas (+ - / * ** // %)
#booleanos (True e False) e operadores comparativos > < >= <= != 
#lógica condicional if() elseif() else
#listas = [1,2,3,4,5]
#métodos para listas -> append, remove, insert, sort
#laços de repetição -> for e while
#funções -> def função():
#recursão -> def função(): função() break

#bibliotecas interessantes e módulos legais :D
#random https://docs.python.org/3/library/random.html
#math https://docs.python.org/3/library/math.html
#unittest https://docs.python.org/3/library/unittest.html

import random
import unittest
import math


dado_6_lados = random.randint(1,6)
print(dado_6_lados)

#testes unitarios -> introdução e TDD!
def teste_unitario_dado(dado):
    assert dado <= 6,"O valor do dado obtido foi maior que 6"
    print("O dado tem o valor <= 6 :D")
    print("Todos os testes passaram!")

teste_unitario_dado(dado_6_lados)



print(math.sqrt(15))
print(math.sin(math.pi/6))
print(math.cos(math.radians(60)))


#numpy
#matplotlib

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
x = np.linspace(0, 10, 100)
y = 4 + np.sin(x)

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

# plt.show()
plt.savefig("matplotlib.png")

#POO


class Pessoa:
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade
    
    def ola(self):
        print("Ola, eu sou "+self.nome+ " e tenho " + str(self.idade) + " anos")

lucas = Pessoa(nome="Lucas",idade=23)
print(lucas.idade)
lucas.ola()


class Retangulo:
    def __init__(self, altura:float, largura:float):
        self.altura = altura
        self.largura = largura

    def area(self):
        return(self.altura * self.largura)

    def perimetro(self):
        return(self.altura * 2 + self.largura * 2)


meu_primeiro_retangulo = Retangulo(altura = 10,largura = 20)
meu_segundo_retangulo = Retangulo(altura = 5,largura = 12)
print(meu_primeiro_retangulo.area())
print(meu_segundo_retangulo.area())