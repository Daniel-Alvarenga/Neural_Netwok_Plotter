print("Neural Network Plotter by Daniel Alvarenga")

import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

espacamento = 0.5

c = 0

neuronios_por_camada = []

print("\nInsira a quantidade de neurônios das camadas (Mínimo 2 camadas):")

neuronios_por_camada = []

while True:
    c += 1
    if c < 3:
        while True:
            try:
                n = int(input(f"- {c}º camada: "))
                if n <= 0:
                    print("Por favor, insira um número inteiro positivo.")
                else:
                    neuronios_por_camada.append(n)
                    break
            except ValueError:
                print("Por favor, insira um número inteiro positivo.")
    else:
        while True:
            try:
                n = int(input(f"- {c}º camada (-1 para plotar): "))
                if n == -1:
                    break
                elif n <= 0:
                    print("Por favor, insira um número inteiro positivo ou -1 para plotar.")
                else:
                    neuronios_por_camada.append(n)
                    break
            except ValueError:
                print("Por favor, insira um número inteiro positivo ou -1 para plotar.")
        if n == -1:
            break

num_camadas = len(neuronios_por_camada)

pos = {}

for camada in range(num_camadas):
    num_neuronios_camada = neuronios_por_camada[camada]
    altura_camada = (num_neuronios_camada - 1) * 5

    for neuronio in range(num_neuronios_camada):
        pos[f'C{camada}_N{neuronio}'] = (50 + (camada * espacamento * 20), altura_camada - neuronio  * 10)


for camada in range(num_camadas - 1):
    for neuronio_camada_atual in range(neuronios_por_camada[camada]):
        for neuronio_proxima_camada in range(neuronios_por_camada[camada + 1]):
            G.add_edge(f'C{camada}_N{neuronio_camada_atual}',
                    f'C{camada + 1}_N{neuronio_proxima_camada}')

largura = 12 + num_camadas * 0.75           

plt.figure(figsize=(largura, 12))
nx.draw(G, pos, node_size=150, node_color='#007FFF', edge_color='#003566', arrows=False, with_labels=False)

arquivo = f"image/imagem{'_'.join(map(str, neuronios_por_camada))}.png"

# Salvar a imagem com fundo preto
plt.savefig(arquivo, facecolor='#000000', bbox_inches="tight", pad_inches=0)
print("\nImagem salva com sucesso em ./image!")

# Salvar a imagem com fundo transparente
# plt.savefig("imagem_fundo.png", transparent=True, bbox_inches="tight", pad_inches=0)

print("\nDaniel Alvarenga - 2023")