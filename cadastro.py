# criação de listas com []
nomes = []
idades = []  
cidades = []

quantidade = int(input("Quantas pessoas você quer cadastrar? "))

for i in range(quantidade):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    cidade = input(f"Digite a cidade de {nome}: ")

    # inserção nas listas com .append()
    nomes.append(nome)
    idades.append(idade)
    cidades.append(cidade)

print("\nPessoas cadastradas:")
for i in range(quantidade):
    maior = "maior de idade" if idades[i] >= 18 else "menor de idade"
    print(f"{nomes[i]}, {idades[i]} anos ({maior}), de {cidades[i]}")

# i representa a pessoa atual no loop
# quando i = 0 → primeira pessoa, i = 1 → segunda pessoa, etc