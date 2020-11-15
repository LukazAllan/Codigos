
# O Guia para o R

## Comentários

Comentários in-line: `#`

## Variáveis

Para associar existem alguns jeitos de associar valores a variáveis:

```R
a  <- 10
b   = 10
10 -> c
c  -> d
```

O padrão é: `<-` para atribuição de variáveis e `=` para atribuição de funções.


## Tipos de Dados

### Character | Texto | Cadeia de caracteres

Texto sempre em aspas duplas

```
"Allan" "Marina" "Lorem Ipsum" "10" "-99.5" "False"
```

### Integer | Números Inteiros

Os números podem ser entendidos de duas formas, uma delas é como número inteiro. 

**Exemplos:**👍🏻

```
0L  66L 110L -78L -4L -8L
```

**Exemplos:**👎🏼

```
'10'  "36"  10.0
```

### Double | Números Reais | Números com ponto flutuante

O `double` é outra forma que o R tem de reconhecer números, aqueles números com vírgula ou ponto decimal. 

**Exemplos:**👍🏻

```
10.0  -35.9  3.14159  0.149
```

**Exemplos:**👎🏻

```
3,14  '10.0' "9,5"
```
