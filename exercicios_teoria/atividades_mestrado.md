### 1 Determine a taxa efetiva MENSAL e ANUAL de juros de uma taxa nominal de 11% ao ano com capitalização mensal? Resposta: 0,92% ao mês e 11,57% ao ano.

```python
def calcula_taxa_efetiva(taxa_nominal_mes, periodo_desejado):
    """
    Calcula a taxa efetiva dada uma taxa nominal mensal e o período desejado.
    
    :param taxa_nominal_mes: Taxa nominal mensal (%)
    :param periodo_desejado: Período desejado (em meses para taxa efetiva anual)
    :return: Taxa efetiva (%)
    """
    taxa_efetiva_mes = (1 + taxa_nominal_mes / 100)
    taxa_efetiva = (taxa_efetiva_mes ** periodo_desejado)
    return (taxa_efetiva - 1) * 100

# Dados do problema
taxa_nominal_anual = 11
taxa_nominal_mes = taxa_nominal_anual / 12  # Convertendo a taxa anual para mensal

# Calculando a taxa efetiva mensal e anual
taxa_efetiva_mensal = calcula_taxa_efetiva(taxa_nominal_mes, 1)
taxa_efetiva_anual = calcula_taxa_efetiva(taxa_nominal_mes, 12)

print(f"Taxa efetiva mensal: {taxa_efetiva_mensal:.2f}%")
print(f"Taxa efetiva anual: {taxa_efetiva_anual:.2f}%")

```

#### 12 Quanto precisamos depositar hoje em um fundo de aplicação para a substituição de um implemento, no valor de R$ 80.000,00 daqui a 2 (dois) anos, se a instituição financeira remunera o capital a uma taxa de 0,56% ao mês? 
```python
def calcular_valor_presente(valor_futuro, taxa_mensal, num_meses):
    """
    Calcula o valor presente necessário para alcançar um valor futuro dado
    uma taxa de juros mensal e o número de meses.
    
    :param valor_futuro: Valor futuro desejado (R$)
    :param taxa_mensal: Taxa de juros mensal (%)
    :param num_meses: Número de meses
    :return: Valor presente necessário (R$)
    """
    valor_presente = valor_futuro / ((1 + taxa_mensal / 100) ** num_meses)
    return valor_presente

# Dados do problema
valor_futuro = 80000.00
taxa_mensal = 0.56
num_meses = 2 * 12  # 2 anos em meses

# Calculando o valor presente
valor_presente = calcular_valor_presente(valor_futuro, taxa_mensal, num_meses)
print(valor_presente)
```
#### 13 Qual o valor presente (VP) das séries de pagamentos não-uniformes apresentadas nas Figuras a seguir. Considere uma taxa de juros (i) igual a 11% ao ano e um horizonte de análise (N) de 5 (cinco) anos. Resposta: (a) R$ 1.031,99; (b) R$ 1.185,55.

O codigo abaixo pode ser utilizado para os exercicio 13, 14 e 15 apenas modificando os valores da lista de fluxo e os juros anuais.

```python
def calcular_valor_presente(lista_fluxo, taxa_anual):
    """
    Calcula o valor presente de uma série de fluxos de caixa futuros.
    
    :param lista_fluxo: Lista de fluxos de caixa futuros (R$)
    :param taxa_anual: Taxa de juros anual (%)
    :return: Valor presente total (R$)
    """
    valor_presente = 0  # Inicializa o valor presente total

    # Itera sobre a lista de fluxos de caixa com seus respectivos índices
    for index, fluxo in enumerate(lista_fluxo):
        index_corrigido = index + 1  # Ajusta o índice para corresponder ao período
        # Calcula o valor presente do fluxo de caixa atual
        valor_presente += fluxo / ((1 + taxa_anual / 100) ** index_corrigido)

    return valor_presente

# Dados do problema
lista_fluxo = [100, 200, 300, 400, 500]
taxa_anual = 11

# Calculando o valor presente
valor_presente = calcular_valor_presente(lista_fluxo, taxa_anual)
print(valor_presente)
```

#### 16 Considere uma taxa de juros de 12,75% ao ano com capitalização mensal. Nesse contexto, determine o valor presente do fluxo de caixa anual exibido na Figura a seguir.

Nesse exemplo é nos dados a taxa de juro nominal, então precisamos calcular a taxa de juro efetiva anual para utilizar a função.

```python
def calcular_valor_presente(lista_fluxo, taxa_anual):
    valor_presente = 0 
    # Itera sobre a lista de fluxos de caixa com seus respectivos índices
    for index, fluxo in enumerate(lista_fluxo):
        index_corrigido = index + 1  # Ajusta o índice para corresponder ao período
        # Calcula o valor presente do fluxo de caixa atual
        valor_presente += fluxo / ((1 + taxa_anual / 100) ** index_corrigido)

    return valor_presente

# Dados do problema
lista_fluxo = [100,150,170,190,210,190,170,150,100]
taxa_anual = (((1 + 12.75/(12*100)) ** 12) -1) * 100 #13.52%

# Calculando o valor presente
valor_presente = calcular_valor_presente(lista_fluxo, taxa_anual)
print(valor_presente)

```

#### 17 Qual o Valor Presente (VP) da série de pagamentos não-uniformes apresentada na Figura a seguir. Considere uma taxa de juros (i) igual a 14,25% ao ano e um horizonte de análise (N) de 5 (cinco) meses. 

Para a questão 17, 18 e 20 temos um modo diferente de calcular a taxa mensal, isso pois temos a taxa de 14,25% com capitalização anual.

```python
def calcular_valor_presente(lista_fluxo, taxa_anual):
    """
    Calcula o valor presente de uma série de fluxos de caixa futuros.
    
    :param lista_fluxo: Lista de fluxos de caixa futuros (R$)
    :param taxa_anual: Taxa de juros anual (%)
    :return: Valor presente total (R$)
    """
    valor_presente = 0  # Inicializa o valor presente total

    # Itera sobre a lista de fluxos de caixa com seus respectivos índices
    for index, fluxo in enumerate(lista_fluxo):
        index_corrigido = index + 1  # Ajusta o índice para corresponder ao período
        # Calcula o valor presente do fluxo de caixa atual
        valor_presente += fluxo / ((1 + taxa_anual / 100) ** index_corrigido)

    return valor_presente

# Dados do problema
lista_fluxo = [100,200,300,400,500]
taxa_anual = 14.25 / 100  # Converte a taxa anual de porcentagem para decimal
taxa_mensal = (1 + taxa_anual) ** (1 / 12) - 1
taxa_mensal_percentual = taxa_mensal * 100  # Converte de volta para porcentagem


# Calculando o valor presente
valor_presente = calcular_valor_presente(lista_fluxo, taxa_mensal)
print(valor_presente)

```
#### 19 Calcule o Valor Presente (VP) do Fluxo de Caixa (FC) mensal indicado no diagrama a seguir, com uma taxa de juros (i) de 1% ao mês, no regime de juros compostos.

```python
def calcular_valor_presente(lista_fluxo, taxa_anual):

    valor_presente = 0  # Inicializa o valor presente total

    # Itera sobre a lista de fluxos de caixa com seus respectivos índices
    for index, fluxo in enumerate(lista_fluxo):
        index_corrigido = index + 1  # Ajusta o índice para corresponder ao período
        # Calcula o valor presente do fluxo de caixa atual
        valor_presente += fluxo / ((1 + taxa_anual / 100) ** index_corrigido)

    return valor_presente

# Dados do problema
lista_fluxo = [10,10,10,10,0,10,10,10]
taxa_mensal = 1 / 100 
taxa_mensal_percentual = taxa_mensal * 100 


# Calculando o valor presente
valor_presente = calcular_valor_presente(lista_fluxo, taxa_mensal)
print(valor_presente)
```

#### Nos exercicios a seguir sera nessesario importar a lib pandas do python para gerar as tabelas de acordo com o input do usuario. O codigo utilizado sera o seguinte:

### Para um sistema de amortização price temos :
```python
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

# Calculando a prestação fixa após o período de carência

for ano in range(1, num_prestacoes + 1):
    if ano <= periodo_carencia:
        juros = saldo_devedor * taxa_juros_anual
        amortizacao = 0
        prestacao = juros
        
        if capitalizacao_carencia:
            saldo_devedor_novo += juros
            saldo_devedor += juros
            prestacao = 0
    else:
        prestacao_fixa = saldo_devedor_novo * (taxa_juros_anual / (1 - (1 + taxa_juros_anual) ** -(num_prestacoes - periodo_carencia)))
        juros = saldo_devedor * taxa_juros_anual
        amortizacao = prestacao_fixa - juros
        prestacao = prestacao_fixa
        saldo_devedor -= amortizacao
    
    # Arredondar os valores para melhor apresentação
    saldo_devedor_inteiro = round(saldo_devedor, 2)
    planilha.append([ano, saldo_devedor_inteiro, round(juros, 2), round(amortizacao, 2), round(prestacao, 2)])

# Criando o DataFrame
df = pd.DataFrame(planilha, columns=["Ano", "Saldo Devedor", "Juros", "Amortização", "Prestação Anual"])

# Exibindo a planilha
print(df)

```
### Para um sistema de amortização sac temos :

```python
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
```
### Para um sistema de amortização SAA temos :
```python
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

```

#### 23 Um produtor rural pretende construir um barracão de máquinas. O valor total da construção está estimado em R$ 200.000,00, com 20% à vista. O saldo restante pode ser financiado em 4 (quatro) prestações anuais, com juros de 11% ao ano. Construir a planilha de desenvolvimento do financiamento, considerando os sistemas a seguir:

Price

![alt text](/assets/images/23A.png)

SAC

![alt text](/assets/images/23b.png)

SAA

![alt text](/assets/images/23c.png)




#### 24	Um produtor rural pretende investir na construção de um barracão para o armazenamento de máquinas, equipamentos e implementos agrícolas. O valor total da construção está estimado em R$ 200.000,00, com 20% à vista. O saldo restante pode ser financiado em 5 prestações anuais, com juros de 11% ao ano. Nesse período está contemplado 2 anos de carência, sem capitalização do saldo devedor por meio do pagamento dos juros. Construir a planilha de desenvolvimento do financiamento, preenchendo os quadros a seguir para cada sistema de amortização (PRICE e SAC).

Price

![alt text](/assets/images/24A.png)

SAC

![alt text](/assets/images/24B.png)

#### 25 Um produtor rural pretende investir na construção de um barracão para o armazenamento de máquinas, equipamentos e implementos agrícolas. O valor total da construção está estimado em R$ 625.000,00, com 20% à vista. O saldo restante pode ser financiado em 5 prestações anuais, com juros de 12,75% ao ano. Nesse período está contemplado 2 anos de carência, com capitalização do saldo devedor, pois não haverá o pagamento de juros nesse período. Construir a planilha de desenvolvimento do financiamento, preenchendo os quadros a seguir para cada sistema de amortização (PRICE e SAC).


price

![alt text](/assets/images/25a.png)

SAC

![alt text](/assets/images/25b.png)

#### 26 e 27 Uma indústria metalúrgica pretende investir na construção de um barracão. O valor total da construção está estimado em R$ 500.000,00, com 10% à vista. O saldo restante pode ser financiado em 5 prestações anuais, com juros de 14,25% ao ano. Nesse período está contemplado 2 anos de carência, com capitalização do saldo devedor, pois não haverá o pagamento de juros nesse período. Construir a planilha de desenvolvimento do financiamento, preenchendo o quadro a seguir para o Sistema de Amortização PRICE.

price com capitalizaçãoo 
<br> 

![alt text](/assets/images/26.png)

<br> 

SAC sem capitalização
<br> 

![alt text](/assets/images/27.png)

#### 28 e 29	Um produtor rural pretende investir na construção de um barracão para o armazenamento de máquinas, equipamentos e implementos agrícolas. O valor total da construção está estimado em R$ 400.000,00, com 15% à vista. O saldo restante pode ser financiado em 5 prestações anuais, com juros de 14,25% ao ano. Nesse período está contemplado 2 anos de carência, sem capitalização do saldo devedor, pois haverá o pagamento de juros nesse período. Nesse contexto, pede-se para construir a planilha de desenvolvimento do financiamento, preenchendo o quadro a seguir para o Sistema de Amortização PRICE.

price com capitalizaçãoo 
<br> 

![alt text](/assets/images/28.png)
<br> 
SAC sem capitalização
<br> 

![alt text](/assets/images/29.png)

#### 30 - 31	Um empreendedor rural pretende investir na construção de um silo para o armazenamento de sua produção de grãos. O valor total da construção está orçado em cerca de R$ 300.000,00, com 25% à vista. O saldo restante pode ser financiado em 4 anos, com juros de 7,5% ao ano. Nesse período está contemplado 2 anos de carência, sem capitalização do saldo devedor, pois haverá o pagamento de juros nesse período. Construir a planilha de desenvolvimento do financiamento, preenchendo o quadro a seguir para o Sistema de Amortização PRICE.

price sem capitalizaçãoo
<br> 

![alt text](/assets/images/30.png)
<br> 
SAC sem capitalização
<br> 

![alt text](/assets/images/31.png)