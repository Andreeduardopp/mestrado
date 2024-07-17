# def calcular_valor_presente(valor_futuro, taxa_mensal, num_meses):

#     valor_presente = valor_futuro / ((1 + taxa_mensal / 100) ** num_meses)
#     return valor_presente

# valor_futuro = 80000.00
# taxa_mensal = 0.56
# num_meses = 2 * 12 

# # Calculando o valor presente
# valor_presente = calcular_valor_presente(valor_futuro, taxa_mensal, num_meses)
# print(valor_presente)

def calcular_valor_presente(lista_fluxo, taxa_anual):

    valor_presente = 0  # Inicializa o valor presente total

    # Itera sobre a lista de fluxos de caixa com seus respectivos índices
    for index, fluxo in enumerate(lista_fluxo):
        index_corrigido = index + 1  # Ajusta o índice para corresponder ao período
        # Calcula o valor presente do fluxo de caixa atual
        valor_presente += fluxo / ((1 + taxa_anual / 100) ** index_corrigido)

    return valor_presente

# Dados do problema
lista_fluxo = [100, 200, 300]
taxa_anual = 15.22

# Calculando o valor presente
valor_presente = calcular_valor_presente(lista_fluxo, taxa_anual)
print(valor_presente)

# def calcular_valor_presente(lista_fluxo, taxa_anual):
#     valor_presente = 0 
#     # Itera sobre a lista de fluxos de caixa com seus respectivos índices
#     for index, fluxo in enumerate(lista_fluxo):
#         index_corrigido = index + 1  # Ajusta o índice para corresponder ao período
#         # Calcula o valor presente do fluxo de caixa atual
#         valor_presente += fluxo / ((1 + taxa_anual / 100) ** index_corrigido)

#     return valor_presente

# # Dados do problema
# lista_fluxo = [100,150,170,190,210,190,170,150,100]
# taxa_anual = (((1 + 12.75/(12*100)) ** 12) -1) * 100 #13.52%

# # Calculando o valor presente
# valor_presente = calcular_valor_presente(lista_fluxo, taxa_anual)
# print(valor_presente) 

# def calcular_valor_presente(lista_fluxo, taxa_anual):
#     """
#     Calcula o valor presente de uma série de fluxos de caixa futuros.
    
#     :param lista_fluxo: Lista de fluxos de caixa futuros (R$)
#     :param taxa_anual: Taxa de juros anual (%)
#     :return: Valor presente total (R$)
#     """
#     valor_presente = 0  # Inicializa o valor presente total

#     # Itera sobre a lista de fluxos de caixa com seus respectivos índices
#     for index, fluxo in enumerate(lista_fluxo):
#         index_corrigido = index + 1  # Ajusta o índice para corresponder ao período
#         # Calcula o valor presente do fluxo de caixa atual
#         valor_presente += fluxo / ((1 + taxa_anual / 100) ** index_corrigido)

#     return valor_presente

# # Dados do problema
# lista_fluxo = [100,200,300]
# taxa_anual = 14.25 / 100  # Converte a taxa anual de porcentagem para decimal
# taxa_mensal = (1 + taxa_anual) ** (1 / 12) - 1
# taxa_mensal_percentual = taxa_mensal * 100  # Converte de volta para porcentagem


# # Calculando o valor presente
# valor_presente = calcular_valor_presente(lista_fluxo, taxa_mensal)
# print(valor_presente)