# TRABALHO APRENDIZAGEM DE MÁQUINA
# Simulador de Investimentos - Caixinha Super Cofrinho

# Alunos:
# Davy Maciel de Souza - Matrícula: 2324290025
# David Martins Peres - Matrícula: 2324290022
# Daniel Francisco - Matrícula: 2324290089
# Thiago Silva Azevedo - Matrícula: 2324290054

# Função para calcular o rendimento bruto com base em juros compostos diários
def calcular_rendimento(valor, dias):
    taxa_ano = 0.1415   # Taxa anual de 14,15%
    taxa_dia = taxa_ano / 365   # Conversão para taxa diária
    valor_final = valor * ((1 + taxa_dia) ** dias)  # Fórmula de juros compostos
    return valor_final

# Função para calcular o IOF com base na tabela regressiva (aplica-se até 30 dias)
def calc_iof(dias, rendimento):
    if dias > 30:
        return 0    # Após 30 dias, IOF é isento
    tabela_iof = {  # Tabela oficial regressiva de IOF (% do rendimento)
        1: 0.96, 2: 0.93, 3: 0.90, 4: 0.86, 5: 0.83, 6: 0.80, 7: 0.76, 8: 0.73, 9: 0.70,
        10: 0.66, 11: 0.63, 12: 0.60, 13: 0.56, 14: 0.53, 15: 0.50, 16: 0.46, 17: 0.43,
        18: 0.40, 19: 0.36, 20: 0.33, 21: 0.30, 22: 0.26, 23: 0.23, 24: 0.20, 25: 0.16,
        26: 0.13, 27: 0.10, 28: 0.06, 29: 0.03, 30: 0.00
    }
    return rendimento * tabela_iof.get(dias, 0.0)   # Aplica a alíquota do dia correspondente

# Função para calcular o IR (Imposto de Renda) com base nos dias aplicados
def calc_ir(dias, rendimento):
    if dias <= 180:
        return rendimento * 0.225   # 22,5%
    elif dias <= 360:
        return rendimento * 0.20    # 20%
    elif dias <= 720:
        return rendimento * 0.175   # 17,5%
    else:
        return rendimento * 0.15    # 15%

# Entrada de dados do usuário
valor = float(input("Valor inicial da aplicação (R$): "))
dias = int(input("Quantidade de dias da aplicação: "))

# Cálculo do rendimento bruto total
valor_com_rendimento = calcular_rendimento(valor, dias)
rendimento = valor_com_rendimento - valor

# Aplicação do IOF (caso necessário)
iof = calc_iof(dias, rendimento)

# Subtrai o IOF do rendimento
rendimento_liquido_iof = rendimento - iof

# Calcula o valor do IR sobre o rendimento já descontado do IOF
ir = calc_ir(dias, rendimento_liquido_iof)

# Valor final que o cliente receberá após descontos
valor_liquido = valor + (rendimento_liquido_iof - ir)

# Exibição dos resultados para o usuário
print("\nResultado da Caixinha Super Cofrinho")
print("Valor Inicial: R$", round(valor, 2))
print("Rendimento Bruto: R$", round(rendimento, 2))
print("Desconto IOF: R$", round(iof, 2))
print("Desconto IR: R$", round(ir, 2))
print("Valor Final Líquido: R$", round(valor_liquido, 2))