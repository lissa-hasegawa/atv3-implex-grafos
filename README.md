# Atividade 3 da Disciplina Implementação Algorítimica - Grafos

Estudantes: Ana Gabriela Silva Barbosa e Elise Lissa Hasegawa

Este projeto é um programa em Python que gera grafos aleatórios com base em um número de vértices e uma probabilidade de conexão. Ele também analisa propriedades do grafo, como o número de arestas, grau mínimo, grau máximo, grau médio e diâmetro.

## Como executar este programa em um ambiente Linux

### Pré-requisitos
- Python versão 3.7 ou superior
- Pip para gerenciamento de pacotes

### Bibliotecas Python necessárias:
- Random
- Collection

## Configuração do Ambiente

1. **Verificar a versão do Python**:
   ```bash
   python3 --version
   ```

2. **Clone este repositório ou copie o código fonte**:
   ```bash
   git clone https://github.com/lissa-hasegawa/atv3-implex-grafos.git
   cd seu-repositorio
   ```

3. **Opcional: Configure um ambiente virtual**:
   Para isolar o ambiente de execução, é recomendável criar um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
## Como Executar

1. Certifique-se de que o arquivo principal se chama, por exemplo, `grafos.py`.

2. Execute o script no terminal:
   ```bash
   python3 grafo.py
   ```

3. **Entrada de parâmetros**:
   Durante a execução, o programa solicitará os seguintes parâmetros:
   - Número inicial de vértices (`ini`): valor inteiro positivo.
   - Número final de vértices (`fim`): valor inteiro maior ou igual ao inicial.
   - Incremento do número de vértices (`stp`): valor inteiro positivo.
   - Probabilidade de conexão (`p`): valor decimal entre 0 e 0.25.

   Exemplo de entrada:
   ```
    ini: 10
    fim: 50
    stp: 10
    p: 0.2
   ```

4. O resultado será exibido da seguinte forma:
   ```
    V       E       gmin    gmax    gmed    diam
    ---------------------------------------------
    10      9       1       4       1.80    6
    20      42      2       8       4.20    4
    30      92      2       10      6.13    3
    40      154     1       12      7.70    4
    50      241     3       16      9.64    4
   ```

## Estrutura do Projeto

O projeto consiste em um único arquivo Python. 
```
.
├── grafo.py          # Arquivo principal contendo o programa
└── README.md         # Este arquivo
```

## Exemplos de Uso

Para gerar grafos de tamanhos diferentes com uma probabilidade de conexão de 0.2:
```bash
python3 grafo.py
```

Entrada de parâmetros:
```
    ini: 10
    fim: 200
    stp: 10
    p: 0.1
```

Saída:
```
    V       E       gmin    gmax    gmed    diam
    ---------------------------------------------
    10      7       0       3       1.40    6
    20      20      0       4       2.00    8
    30      39      0       7       2.60    6
    40      75      0       9       3.75    7
    50      107     0       8       4.28    5
    60      185     2       15      6.17    4
    70      247     2       12      7.06    4
    80      344     1       16      8.60    4
    90      407     3       16      9.04    4
    100     486     4       17      9.72    4
    110     598     5       20      10.87   4
    120     745     3       22      12.42   4
    130     828     3       26      12.74   4
    140     986     5       25      14.09   3
    150     1125    7       25      15.00   3
    160     1206    6       25      15.07   3
    170     1441    7       31      16.95   4
    180     1659    8       30      18.43   3
    190     1791    8       33      18.85   3
    200     2026    10      32      20.26   3
```
