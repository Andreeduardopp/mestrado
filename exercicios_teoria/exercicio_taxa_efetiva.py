def calcula_taxa_efetiva(taxa_nominal_mes, periodo_desejado):
    taxa_efetiva_mes = (1 + taxa_nominal_mes / 100)
    taxa_efetiva = (taxa_efetiva_mes ** periodo_desejado)
    return (taxa_efetiva - 1) * 100

# Dados do problema
taxa_nominal_anual = 14.25
taxa_nominal_mes = taxa_nominal_anual / 12  # Convertendo a taxa anual para mensal
print(taxa_nominal_mes)
# Calculando a taxa efetiva mensal e anual
taxa_efetiva_mensal = calcula_taxa_efetiva(taxa_nominal_mes, 1)
taxa_efetiva_anual = calcula_taxa_efetiva(taxa_nominal_mes, 12)

print(f"Taxa efetiva mensal: {taxa_efetiva_mensal:.2f}%")
print(f"Taxa efetiva anual: {taxa_efetiva_anual:.2f}%")


