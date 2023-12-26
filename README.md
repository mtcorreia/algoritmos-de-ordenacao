# Algoritmos de Ordenação - Python.
<b>Nome do Projeto:</b> algoritomos-de-ordenacao<br/>
<b>Descrição Resumida:</b> Um estudo dirigido e produzido para o aprofundamento nos <b>Algoritmos de Ordenação</b> na linguagem Python.

## Tecnologias Usadas
- <b>Linguagem:</b> Python.
- <b>IDE:</b> Visual Studio Code.

## O Estudo por trás dos Algoritmos de Ordenação:
### Bubble Sort.
<b>Definição:</b> A classificação por bolha, ou <b>Bubble Sort</b>, é um algoritmo básico para organizar uma sequência de números ou outros elementos na ordem correta. O método funciona examinando cada conjunto de elementos adjacentes na string/lista, da esquerda para a direita, trocando suas posições se estiverem fora de ordem. O algoritmo então repete esse processo até que possa percorrer toda a string/lista e não encontrar dois elementos que precisem ser trocados.

<b>Funcionamento:</b> 
1. Em uma matriz não classificada de 5 elementos, comece com os dois primeiros elementos e classifique-os em ordem crescente. (Compare o elemento para verificar qual é o maior).

2. Compare o segundo e o terceiro elemento para verificar qual é o maior e classifique-os em ordem crescente.

3. Compare o terceiro e o quarto elemento para verificar qual é o maior e classifique-os em ordem crescente.

4. Compare o quarto e o quinto elemento para verificar qual é o maior e classifique-os em ordem crescente.

<b>OBS</b>: Repita as etapas 1–4 até que não sejam necessárias mais trocas.

### Selection Sort.
<b>Definição:</b> A ordenação por seleção, ou <b>Selection Sort</b>, é um algoritmo de ordenação baseado em se passar sempre o menor valor do vetor para a primeira posição, depois o de segundo menor valor para a segunda posição, e assim é feito sucessivamente com os j - 1 elementos restantes, até os últimos dois elementos.

<b>Funcionamento:</b>
1. Considere o seguinte exemplo de lista.
<i>lista = [9, 7, 8, 1, 2, 0, 4].</i>

2. O primeiro laço o índice inicial é 0. Percorre-se todo o vetor até achar o menor elemento, neste caso o número zero. O zero passa para a posição inicial do vetor que na primeira iteração do laço é 0.
<i>lista = [0, 7, 8, 1, 2, 9, 4]</i>

3. Ao fim do laço interno, o laço externo incrementa uma unidade, agora a posição inicial da lista passa a ser 1, pois o zero já se encontra no lugar dele, não é preciso mais fazer verificações pois ele é o menor elemento desta lista. Agora o processo se repete, buscando o segundo menor elemento, neste caso o um.
<i>lista = [0, 1, 8, 7, 2, 9, 4]</i>

4. Consequentemente o terceiro menor, quarto menor e assim sucessivamente, até a lista está devidamente ordenado.
<i>lista = [0, 1, 2, 4, 7, 8, 9]</i>
