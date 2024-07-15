import pandas as pd

# Dados do problema
valor_total = float(input('Insira o valor total financiado: '))
percentual_entrada = float(input('Percentual de entrada em %: ')) / 100
taxa_juros_anual = float(input('Insira a taxa de juro anual em %: ')) / 100  # Dividindo por 100 para obter a taxa decimal
num_prestacoes = int(input('Insira o número de prestações: '))

# Calculando valores iniciais
valor_entrada = valor_total * percentual_entrada
saldo_financiado = valor_total - valor_entrada

# Inicializando a lista para armazenar os dados da planilha
planilha = []

# Saldo devedor inicial
saldo_devedor = saldo_financiado

for ano in range(1, num_prestacoes + 1):
    if ano < num_prestacoes:
        juros = saldo_devedor * taxa_juros_anual
        amortizacao = 0
        prestacao = juros
    else:
        juros = saldo_devedor * taxa_juros_anual
        amortizacao = saldo_devedor
        prestacao = juros + amortizacao
        saldo_devedor = 0  # No último ano, o saldo devedor se torna zero após a amortização

    # Arredondar os valores para melhor apresentação
    planilha.append([ano, round(saldo_devedor, 2), round(juros, 2), round(amortizacao, 2), round(prestacao, 2)])

# Criando o DataFrame
df = pd.DataFrame(planilha, columns=["Ano", "Saldo Devedor", "Juros", "Amortização", "Prestação Anual"])

# Exibindo a planilha
print(df)
