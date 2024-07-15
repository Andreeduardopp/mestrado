import pandas as pd

# Dados do problema
valor_total = float(input('Insira o valor total financiado: '))
percentual_entrada = float(input('Percentual de entrada: '))
taxa_juros_anual = float(input('Insira a taxa de juro anual: ')) / 100  # Dividindo por 100 para obter a taxa decimal
num_prestacoes = int(input('Insira o número de prestações: '))
periodo_carencia = int(input('Insira o período de carência (em anos): '))
capitalizacao_carencia = input('A carência terá capitalização de juros? (s/n): ').strip().lower() == 's'

# Calculando valores iniciais
valor_entrada = valor_total * percentual_entrada
saldo_financiado = valor_total - valor_entrada

# Inicializando a lista para armazenar os dados da planilha
planilha = []

# Saldo devedor inicial
saldo_devedor = saldo_financiado
saldo_devedor_novo = saldo_devedor
# Calculando a amortização constante após o período de carência

for ano in range(1, num_prestacoes + 1):
    juro_acumulado = 0
    if ano <= periodo_carencia:
        juros = saldo_devedor * taxa_juros_anual
        amortizacao = 0
        prestacao = juros
        
        if capitalizacao_carencia:
            saldo_devedor_novo += juros
            saldo_devedor += juros
            prestacao = 0

    else:
        amortizacao = saldo_devedor_novo / (num_prestacoes - periodo_carencia)
        juros = saldo_devedor * taxa_juros_anual
        prestacao = amortizacao + juros
        saldo_devedor -= amortizacao
    
    # Arredondar os valores para melhor apresentação
    saldo_devedor_inteiro = round(saldo_devedor, 2)
    planilha.append([ano, saldo_devedor_inteiro, round(juros, 2), round(amortizacao, 2), round(prestacao, 2)])

# Criando o DataFrame
df = pd.DataFrame(planilha, columns=["Ano", "Saldo Devedor", "Juros", "Amortização", "Prestação Anual"])

# Exibindo a planilha
print(df)
