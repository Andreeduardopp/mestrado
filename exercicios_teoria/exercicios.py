import pandas as pd

# Resolução para amortização price

valor_total = float(input('insira o valor total financiado: '))
percentual_entrada = float(input('Percentual de entrada: '))
taxa_juros_anual = float(input('insira a taxa de juro anual: '))
num_prestacoes = int(input('insira o numero de prestações: '))

# Calculando valores iniciais
valor_entrada = valor_total * percentual_entrada
saldo_financiado = valor_total - valor_entrada

# Calculando a prestação anual
i = taxa_juros_anual
n = num_prestacoes
PMT = (saldo_financiado * i) / (1 - (1 + i) ** -n)

# Inicializando a lista para armazenar os dados da planilha
planilha = []

# Saldo devedor inicial
saldo_devedor = saldo_financiado

for ano in range(1, num_prestacoes + 1):
    juros = saldo_devedor * i
    amortizacao = PMT - juros
    saldo_devedor -= amortizacao
    
    # Adicionando os dados na planilha
    planilha.append([ano, round(saldo_devedor), juros, amortizacao, PMT])

# Criando o DataFrame
df = pd.DataFrame(planilha, columns=["Ano", "Saldo Devedor", "Juros", "Amortização", "Prestação Anual"])

# Exibindo a planilha
print(df)

