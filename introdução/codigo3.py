# Montante de juros composto

valorPrimario = float(input("Digite o valor principal: "))
taxa = float(input("Digite a taxa de juros (em decimal): "))
periodos = int(input("Digite o número de períodos: "))
# Exemplo: 1000 . (1+0.05)² = 1102.50
# O número 1 somado a taxa de juros, é para somar ao montante após multiplicar
montante = valorPrimario * (1+taxa) ** periodos
juros = montante - valorPrimario

# Para formatações usando f-strings
# Exemplo: f"{:.3f}" o numero representa a quantidade de casas decimais
print(f"O montante é: R${montante:.2f}")
print(f"O valor do juros é: R${juros:.2f}")