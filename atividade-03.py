import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
idades = []
alturas = []
pesos = []
sobrenomes = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break

    sobrenome = input("digite seu sobrenome( ou digite 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    sobrenomes.append(sobrenome)

    def calcular_imc(peso, altura):
        """calcula o índice de massa corporal(IMC)."""
        return peso / (altura ** 2)
    
    def classificar_IMC(imc):
        """classifica o IMC em categorias."""
        if imc < 18.5:
            return "abaixo do peso"
        elif 18.5 <= imc < 30:
            return "peso normal"
        elif 25 <= imc < 30:
            return "sobrepeso"
        else:
            return "Obesidade"
    print("/nResultados:")

# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i+1}:")
    print(f"Nome:", nomes[i], sobrenomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")

#calculando o imc    
imc = calcular_imc(pesos[i], alturas[i])

#classificando o imc
classificacao = classificar_IMC(imc)

#exibindo resultados
print(f"IMC:  {imc:.2f}")
print(f"classificação: {classificacao}\n")

