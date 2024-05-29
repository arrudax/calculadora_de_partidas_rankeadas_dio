# desafio_classificador_heroi

Para utilizar deve criar uma Matriz de de objetos com o nickname de 'heros', quantidade de vitorias e quantidade de derrotas.


lista_rank_herois = [
    {'nickname':'Igor', 'vitorias':30, "derrotas":20},
    {'nickname':'Pablo', 'vitorias':39, "derrotas":20},
    {'nickname':'Marley', 'vitorias':61, "derrotas":20},
    {'nickname':'Prisley', 'vitorias':41, "derrotas":20},
    {'nickname':'Bob', 'vitorias':71, "derrotas":20},
    {'nickname':'Claudio', 'vitorias':91, "derrotas":20},
    {'nickname':'Odete', 'vitorias':101, "derrotas":20},
    {'nickname':'Paola', 'vitorias':111, "derrotas":20},
    {'nickname':'Lopes', 'vitorias':121, "derrotas":20},
]


para ver os prints:
for heroi in lista_rank_herois:
    get_rank(quantidadeVitorias=heroi['vitorias'], quantidadeDerrotas=heroi['derrotas'])
