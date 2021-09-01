# AnalisadorLexico
Primeiro problema do MI de Algoritmos

## Requisitos
- Ter o Python 3.9.6 instalado;
- Ter criado a pasta com o nome "input" criada no mesmo repositório do arquivo AnalisadorLexico.py;
- Nomear os arquivos de entrada com o nome "entradaX.txt" onde o X será números inteiros positivos em sequência começando do 1. Exemplo: "entrada1.txt".
- Os arquivos são pegos de forma sequencial, ou seja, se houver os arquivos: "entrada1.txt", "entrada2.txt" e "entrada4.txt", a saída será: "saida1.txt" e "saida2.txt".

## Tabela da Estrutura Léxica
![Tabela da estrutura lexica.png](https://github.com/WilliamOSoares/AnalisadorLexico/blob/main/Imagens/Tabela%20da%20estrutura%20lexica.png)

- Na cadeia de caracteres e no caractere, o \, ', ", 0, a, b, t, f, n e r serão aceitos se tiver o \ antes destes caracteres.

## Tabela ASCII usada como base para o desenvolvimento
![ASCII.jpg](https://github.com/WilliamOSoares/AnalisadorLexico/blob/main/Imagens/ASCII.jpg)

## Diagrama de Transição de estados
![Analisador Lexico Diagrama Estados.jpeg](https://github.com/WilliamOSoares/AnalisadorLexico/blob/main/Imagens/Analisador%20Lexico%20Diagrama%20Estados.jpeg)

- Se ocorrer a entrada de um símbolo que não corresponde a regra da transição de estados, o estado terá uma saída e retornará ao estado inicial para analisar o símbolo.

