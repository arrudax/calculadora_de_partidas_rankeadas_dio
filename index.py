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

def get_rank(quantidadeVitorias: int, quantidadeDerrotas:int):
    saldoVitorias = quantidadeVitorias - quantidadeDerrotas
    nivel = ""
    
    if saldoVitorias <= 10:
        nivel = "Ferro"
    elif saldoVitorias >= 11 and saldoVitorias <= 20:
        nivel = "Bronze"
    elif saldoVitorias >= 21 and saldoVitorias <= 50:
        nivel = "Prata"
    elif saldoVitorias >= 51 and saldoVitorias <= 80:
        nivel = "Ouro"
    elif saldoVitorias >= 81 and saldoVitorias <= 90:
        nivel = "Platina"
    elif saldoVitorias >= 91 and saldoVitorias <= 100:
        nivel = "Ascendente"
    elif saldoVitorias >= 101:
        nivel = "Imortal"
        
    return f"O Herói tem de saldo de {saldoVitorias} está no nível de {nivel}"
 
            
for heroi in lista_rank_herois:
    rank = get_rank(quantidadeVitorias=heroi['vitorias'], quantidadeDerrotas=heroi['derrotas'])
    print(rank)


