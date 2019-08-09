# Desafios resolvidos do site Dojo Puzzles

## Estátisticas Simples - [Resolução](https://github.com/grbalmeida/dojo-puzzles/blob/master/simple-statistics/simple_statistics.py)

Sua tarefa é processar uma seqüência de números inteiros para determinar as seguintes estatísticas:

* Valor mínimo
* Valor máximo
* Número de elementos na seqüência
* Valor médio

Por exemplo para uma seqüência de números "6, 9, 15, -2, 92, 11", temos como saída:

* Valor mínimo: -2
* Valor máximo: 92
* Número de elementos na seqüência: 6
* Valor médio: 18.1666666

[Link do desafio](http://dojopuzzles.com/problemas/exibe/calculando-estatisticas-simples/)

## Caixa Eletrônico - [Resolução](https://github.com/grbalmeida/dojo-puzzles/blob/master/cash-machine/cash_machine.py)

Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico. Os requisitos básicos são os seguintes:

* Entregar o menor número de notas;
* É possível sacar o valor solicitado com as notas disponíveis;
* Saldo do cliente infinito;
* Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
* Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00

Exemplos:

* Valor do Saque: R$ 30,00 – Resultado Esperado: Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
* Valor do Saque: R$ 80,00 – Resultado Esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00.

[Link do Desafio](http://dojopuzzles.com/problemas/exibe/caixa-eletronico/)

## FizzBuzz - [Resolução](https://github.com/grbalmeida/dojo-puzzles/blob/master/fizz-buzz/fizz_buzz.py)

Neste problema, você deverá exibir uma lista de 1 a 100, um em cada linha, com as seguintes exceções:

* Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do número;
* Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do número;
* Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do número'.

[Link do Desafio](http://dojopuzzles.com/problemas/exibe/fizzbuzz/)

## Jokenpo - [Resolução](https://github.com/grbalmeida/dojo-puzzles/blob/master/jokenpo/jokenpo.py)

Jokenpo é uma brincadeira japonesa, onde dois jogadores escolhem um dentre três possíveis itens: Pedra, Papel ou Tesoura.

O objetivo é fazer um juiz de Jokenpo que dada a jogada dos dois jogadores informa o resultado da partida.

As regras são as seguintes:

* Pedra empata com Pedra e ganha de Tesoura
* Tesoura empata com Tesoura e ganha de Papel
* Papel empata com Papel e ganha de Pedra

[Link do Desafio](http://dojopuzzles.com/problemas/exibe/jokenpo/)

## Entradas no Banco - [Resolução](https://github.com/grbalmeida/dojo-puzzles/blob/master/bank-entries/bank_entries.py)

Todas as vezes que alguém passa na porta do maior banco da cidade de Pirenópolis, é gravado em um arquivo de log a data e a hora da abertura da porta.

Cada registro no arquivo de log possui o seguinte formato:

[YYYY-mm-dd H:i:s] - Abertura da Porta OK

O gerente do banco precisa saber quantas pessoas entraram no banco no horário de expediente, para isso ele solicitou que você faça um programa que verifique se o registro de entrada é válido e se a hora se encontra dentro do intervalo de funcionamento do banco, das 10:00:00 até as 16:00:00.

[Link do Desafio](http://dojopuzzles.com/problemas/exibe/entradas-no-banco/)

## Ano Bissexto - [Resolução](https://github.com/grbalmeida/dojo-puzzles/blob/master/leap-year/leap_year.py)

A cada 4 anos, a diferença de horas entre o ano solar e o do calendário convencional completa cerca de 24 horas (mais exatamente: 23 horas, 15 minutos e 864 milésimos de segundo). Para compensar essa diferença e evitar um descompasso em relação às estações do ano, insere-se um dia extra no calendário e o mês de fevereiro fica com 29 dias. Essa correção é especialmente importante para atividades atreladas às estações, como a agricultura e até mesmo as festas religiosas.

Um determinado ano é bissexto se:

O ano for divisível por 4, mas não divisível por 100, exceto se ele for também divisível por 400.
Exemplos:

São bissextos por exemplo:

* 1600
* 1732
* 1888
* 1944
* 2008

Não são bissextos por exemplo:

* 1742
* 1889
* 1951
* 2011

Escreva uma função que determina se um determinado ano informado é bissexto ou não.

[Link do Desafio](http://dojopuzzles.com/problemas/exibe/ano-bissexto/)

## Intervalos - [Resolução](https://github.com/grbalmeida/dojo-puzzles/blob/master/intervals/intervals.py)

Dado uma lista de números inteiros, agrupe a lista em um conjunto de intervalos

Exemplo:

Entrada: 100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150

Saída: [100-105], [110-111], [113-115], [150]

[Link do Desafio](http://dojopuzzles.com/problemas/exibe/intervalos/)