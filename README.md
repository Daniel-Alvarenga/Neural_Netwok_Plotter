# Neural_Netwok_Plotter
Customizable neural network plotter

Com esse script, você pode criar uma representação gráfica de sua rede neural, com os neurônios, camadas e ligações entre camadas.
O objetivo do projeto é auxiliar em uma rápida criação de imagens assim para maior agilidade em criação de documentações de projetos que as usam.
O funcionamento é relativamente simples, onde se usa a biblioteca networkx para criação do grafo, e cálculos simples para criar posições adequadas para cada neurônio.
A imagem é por fim passada para um objeto matplotlib e salva na pasta de images com um nome descritivo com base na quantidade de neurônios de cada camada.

<p align="center">
  <img src="https://github.com/Daniel-Alvarenga/Neural_Netwok_Plotter/assets/128755697/deabf8f4-e1cd-4902-9999-2196475c60e6"/>
</p>

## Utilização

Para utilizar este projeto, siga os passos abaixo:

1. **Clone o Repositório:** Para começar, clone o repositório do projeto para o seu sistema local. Use o seguinte comando no terminal:
```bash    
git clone https://github.com/Daniel-Alvarenga/Neural_Netwok_Plotter
```

    
2. **Navegue para a Pasta do Projeto:** Navegue para a pasta do projeto usando o comando `cd`. Por exemplo:
```bash
cd Neural_Netwok_Plotter
 ```
    
3. **Crie um Ambiente Virtual (Opcional):** Recomenda-se criar um ambiente virtual para isolar as dependências deste projeto. Use `venv` (Python 3) ou `virtualenv`:
 ```bash
python -m venv venv
 ```

Ative o ambiente virtual:
    

 - No Windows:
```bash
venv\Scripts\activate
``` 
    
 - No macOS e Linux: 
```bash       
source venv/bin/activate
```

1. **Instale as Dependências:** Certifique-se de que as dependências necessárias estejam instaladas. Você pode usar o `requirements.txt` fornecido para instalar todas as dependências de uma vez:
 ```bash
 pip install -r requirements.txt
  ```
2. **Execute o `load.py`:** Após configurar o ambiente e instalar as dependências, você pode executar o `load.py` para carregar o modelo treinado e reconhecer dígitos em novas imagens. Use o seguinte comando: 
   ```bash   
    python plotter.py
    ```
Siga as instruções para que o script tenha os dados de sua rede. Ao finalizar entrando com -1, você terá a imagem salva na pasta image.
