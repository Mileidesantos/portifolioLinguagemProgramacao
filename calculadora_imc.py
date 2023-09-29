# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def obter_dados_usuario():
    while True:
        try:    
# Solicita entrada do usuário
            peso = float(input("Digite seu peso em kg: "))
            altura = float(input("Digite sua altura em metros: "))
            return peso, altura
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")

def avaliar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 24.9 <= imc < 29.9:
        return "Sobrepeso"
    elif 29.9 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 34.9 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"
        
# Calcula o IMC
peso, altura = obter_dados_usuario()
imc = calcular_imc(peso, altura)
classificacao = avaliar_imc(imc)

# Exibe o resultado
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
