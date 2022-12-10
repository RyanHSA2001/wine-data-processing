# wine-data-process

Este trabalho foi feito com o intuito de exercitar a manipulação de dados em python.

O dataset escolhido se trata de um conjunto de dados relacionados com a variante tinto do vinho português "Vinho Verde". Fonte do dataset: https://archive.ics.uci.edu/ml/datasets/Wine+Quality

Variáveis de entrada (com base em testes físico-químicos):
1 - acidez fixa
2 - acidez volátil
3 - ácido cítrico
4 - açúcar residual
5 - cloretos
6 - dióxido de enxofre livre
7 - dióxido de enxofre total
8 - densidade
9 - pH
10 - sulfatos
11 - álcool
Variável de saída (com base em dados sensoriais):
12 - qualidade (pontuação entre 0 e 10)

## Funcionamento

O programa lê o conjunto de dados utilizando a biblioteca Pandas. Após a leitura as colunas do dataset são renomeadas para nomes em português, e então é feita a primeira classificação dos dados. A partir de um *for* que percorre o dataset, o programa analisa sua quantidade de açucar residual da qual segundo a **LEI Nº 7.678, DE 8 DE NOVEMBRO DE 1988** classifica o vinho entre Seco, Meio-Seco e Suave. É realizada também uma classificação apartir da quantidade de álcool presente no vinho entre Leve, Médio, Encorpado e Pesado. Uma vez tendo essas duas colunas o programa mostra a média dos compostos, o vinho mais forte e o mais fraco presente neste conjunto de dados. Por fim as colunas que foram classificadas são exibidas graficamente com a biblioteca Plotly.
