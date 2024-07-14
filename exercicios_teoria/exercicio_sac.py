import pandas as pd

# Dados do problema
valor_total = float(input('insira o valor total financiado: '))
percentual_entrada = float(input('Percentual de entrada: '))
taxa_juros_anual = float(input('insira a taxa de juro anual: '))
num_prestacoes = int(input('insira o numero de prestações: '))

# Calculando valores iniciais
valor_entrada = valor_total * percentual_entrada
saldo_financiado = valor_total - valor_entrada

# Calculando a amortização constante
amortizacao = saldo_financiado / num_prestacoes

# Inicializando a lista para armazenar os dados da planilha
planilha = []

# Saldo devedor inicial
saldo_devedor = saldo_financiado

for ano in range(1, num_prestacoes + 1):
    juros = saldo_devedor * taxa_juros_anual
    prestacao = amortizacao + juros
    saldo_devedor -= amortizacao
    
    # Arredondar os valores para melhor apresentação
    saldo_devedor_inteiro = round(saldo_devedor)
    planilha.append([ano, saldo_devedor_inteiro, round(juros, 2), round(amortizacao, 2), round(prestacao, 2)])

# Criando o DataFrame
df = pd.DataFrame(planilha, columns=["Ano", "Saldo Devedor", "Juros", "Amortização", "Prestação Anual"])

# Exibindo a planilha
print(df)