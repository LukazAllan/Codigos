# Guia do Python 3
-----
## Comandos Básicos

**`print()`**: Para escrever na tela.

**`input()`**: Para pedir pro usuário digitar. Sempre que pega o input, ele converte para texto `string`
 

## Comentários

É possivel fazer comentários em linha usando _#_:

```
# Pegando o nome do usuário
nome = input('Digite seu nome: ') 
```
-----

## Variáveis

Para guardar uma informação precisamos saber onde vamos guardar. Por exemplo, para armazenar uma idade, vamos criar uma variável `idade` da seguinte forma:

```
idade = 18
```

**Dica para nome de variáveis:**
  
 - Não seja um programador alfabeto. Crie um nome para as variáveis de acordo com o que vão guardar.
 - Nunca ponha o número no início do nome da variável.
 - Não bote letras com acento.

## Tipos de Dados

### String | Texto | Cadeia de caracteres

Textos para o python são representados com aspas simples (`''`) e aspas duplas (`""`), estes são exemplos de texto:

```
'Allan' "Marina" "Lorem Ipsum" '10' "-99.5" "False"
```

### Int | Números Inteiros

Os números podem ser entendidos de duas formas, uma delas é com `int` ou como número inteiro. 

**Exemplos:**👍🏻

```
0  66 110 -78 -4 -8
```

**Exemplos:**👎🏼

```
'10'  "36"
```

E pode converter para número inteiro:
```
idade = int(input('Digite sua idade: ')
```


### Float | Números Reais | Números com ponto flutuante

O `float` é outra forma que o Python tem de reconhecer números, aqueles números com vírgula ou ponto decimal. 

**Exemplos:**👍🏻

```
10.0  -35.9  3.14159  0.149
```

**Exemplos:**👎🏻

```
3,14  '10.0' "9,5"
```

E pode converter para número real:

```
peso = float(input('Digite seu peso: ')
```