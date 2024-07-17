### 1 Qual a importância/contribuição da Engenharia Econômica para a sua área de conhecimento/estudo e/ou para o desenvolvimento de futuras atividades/habilidades profissionais?
 - A Engenharia Econômica desempenha um papel crucial na
área de engenharia civil e no desenvolvimento de atividades profissionais, principalmente em
projetos de orçamento e gestão financeira. Na engenharia civil, é essencial considerar
princípios da engenharia econômica, como cálculo da variação do capital ao longo do tempo e
análise de juros, para assegurar que os projetos sejam financeiramente viáveis e sustentáveis.

- Trabalhando atualmente com softwares para instituições financeiras e cooperativas de crédito que
oferecem empréstimos e financiamentos de grande valor, a importância da engenharia econômica se
torna ainda mais evidente. O conhecimento em taxas de juros, amortização e outros conceitos de
engenharia econômica é fundamental para desenvolver soluções que atendam às necessidades dessas
instituições e de seus clientes, e além disso, compreender se essas soluções estão se comportando de
acordo com a teoria.

### 2 Explique, COM SUAS PALAVRAS, o que é preciso fazer para avaliar de forma adequada aviabilidade econômica de um Projeto de Investimento (PI) na sua área de conhecimento/estudo.

- Para a análise de viabilidade de software é necessário primeiro que a empresa faça um
estudo de mercado para identificar o potencial e a demanda de tal investimento, Após essa
analise deve ser feito uma estimativa do custo desse projeto com a receita que será gerada do
mesmo, para que assim seja descartada ideia que apesar de plausíveis não são
economicamente sustentáveis para a empresa, além disso, com essa análise será
possível calcular um tempo de retorno do investimento inicial como também diversas outras
métricas que serão importantes fatores de decisão para os stock holders da empresa. Por
último e não menos importante, é necessário serem levados em conta os riscos do investimento
e as variáveis que terão maior impacto no processo de desenvolvimento desse projeto, para
que assim possam ser pensados em planos de mitigação e riscos e gastos.

### 3 Defina, COM SUAS PALAVRAS, o princípio básico da Matemática Financeira.
- Insira sua resposta aqui. O princípio básico da matemática financeira está centrado na ideia de
que o valor do dinheiro varia ao longo do tempo. Para se lidar com valores monetários em
diferentes períodos, é essencial considerar fatores como inflação e juros.

### 4 Defina, COM SUAS PALAVRAS, o conceito e a fórmula básica/fundamental de juros, independente do regime de capitalização (simples, compostos ou contínuos). Na sequência, diferencie juros simples de juros compostos.

- Juro é o valor que deve ser pago pelo uso do capital ao longo do tempo, ou seja, valor
adicional pago sobre um empréstimo ou investimento.
A formula básica para se calcular os juros é (valor do juro = capital inicial * taxa de juro *
Número de períodos).
- A diferença entre os juros compostos e simples é que, nos juros simples, a taxa de juros é
aplicada apenas ao capital inicial. Isso significa que, se temos um número de períodos igual a
vinte, a taxa de juros será aplicada ao capital inicial vinte vezes, resultando em um crescimento
linear dos juros ao longo do tempo.
- Por outro lado, nos juros compostos, a taxa de juros é aplicada ao valor inicial somado ao
juro acumulado dos períodos anteriores. Isso significa que a cada período a taxa de juros é
aplicada a um valor maior, pois inclui os juros acumulados. Esse processo resulta em um
crescimento exponencial do montante, fazendo com que o valor final seja significativamente
maior do que no regime de juros simples, especialmente em períodos mais longos.

### 5 Comente sobre a diferença entre uma taxa de juros nominal e uma taxa de juros efetiva. Na sequência, explique qual(is) a(s) condição(ões) para que duas taxas efetivas de juros sejam equivalentes?
- Em uma taxa de juro nominal, o período a que o juro se refere não coincide com o período
de capitalização, ou seja, podemos ter um juro de 12% ao ano que é capitalizado mensalmente.
Já em uma taxa de juro efetiva, o juro será sempre referenciado no mesmo período em que se
ocorre a capitalização, ou seja, no mesmo exemplo acima, teremos um juro de um por cento ao
mês. As taxas são consideradas equivalentes se resultarem no mesmo valor futuro para o
mesmo inicial e período, apesar de suas diferentes frequências de capitalização.

### 6 Descreva as principais características dos sistemas de amortização PRICE e SAC.
- No sistema de amortização price temos como caracteristicas parcelas com valores fixos e
uma amortização crescente, pois no inicio a maior parte do valor pago nas parcelas sera
referente ao juro (cobrado em cima do saldo devedor). Ja o sistema SAC propõem um valor de
amortização constante do saldo devedor, fazendo assim com que as parcelas iniciais sejam
mais altas, isso, pois o juro é maior nas primeiras parcelas.

### 7 Explique, COM SUAS PALAVRAS, qual a diferença conceitual entre AMORTIZAÇÃO e PRESTAÇÃO. Além disso, estabeleça a relação matemática (fórmula) entre PRESTAÇÃO, JUROS e AMORTIZAÇÃO.
- Uma prestação é nada mais do que a parcela que sera paga de uma divida, ou seja, se
temos uma divida que sera paga em 12 vezes de 1000 reais, a prestação sera é mil reais. Ja a
amortização é o valor da prestação decrescido dos juros , ou seja, é o valor que ira diminuir do
montante inicial da divida. A relação matemática entre os três é Prestação = amortização + juro

### 10 Determine a taxa efetiva MENSAL e ANUAL de juros de uma taxa nominal de 11% ao ano com capitalização mensal? Resposta: 0,92% ao mês e 11,57% ao ano.

Nessa questão precisamos apenas de um script simples que calcula a taxa efetiva de acordo com a taxa nominal.

```python
def calcula_taxa_efetiva(taxa_nominal_mes, periodo_desejado):
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
 - ### resposta:  Taxa efetiva mensal é 0,92% e anual 11,57%    

#### 12 Quanto precisamos depositar hoje em um fundo de aplicação para a substituição de um implemento, no valor de R$ 80.000,00 daqui a 2 (dois) anos, se a instituição financeira remunera o capital a uma taxa de 0,56% ao mês? 
```python
def calcular_valor_presente(valor_futuro, taxa_mensal, num_meses):

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

 - ### resposta:  Valor presente igual a 69965,45 reais.    


#### 13 Qual o valor presente (VP) das séries de pagamentos não-uniformes apresentadas nas Figuras a seguir. Considere uma taxa de juros (i) igual a 11% ao ano e um horizonte de análise (N) de 5 (cinco) anos. Resposta: (a) R$ 1.031,99; (b) R$ 1.185,55.

O codigo abaixo pode ser utilizado para os exercicio 13, 14 e 15 apenas modificando os valores da lista de fluxo e os juros anuais.
[ARQUIVO CODIGO](/exercicios_teoria/exercicio_valor_presente.py)
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
lista_fluxo = [100, 200, 300, 400, 500] # pode ser alterada de acordo
taxa_anual = 11 # pode ser alterado

# Calculando o valor presente
valor_presente = calcular_valor_presente(lista_fluxo, taxa_anual)
print(valor_presente)
```

 - ### Resposta 13 a = R$1031,99 .
- ### Resposta 13 B = R$1185,55 .
- ### Resposta 14  = R$977.23 .
- ### Resposta 15  = 
  nessa questão temos que primeiro calcular a taxa efetiva mensal, essa sera de 1,19%, então utilizando a equação chegamos a um valor presente de  R$977.1436,48.


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
 - ### resposta 16 : R$ 791,56

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
 - ### resposta 17 : R$ 1499,38
 - ### resposta 18 : R$ 433.769

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
 - ### resposta 18 : R$ 67,00

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