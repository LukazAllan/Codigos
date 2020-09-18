#include <stdio.h>
#include <stdlib.h>

/*
1. Durante esses meses, o professor 
Marcelo resolveu desenvolver sistemas em 
home office (ele não fez isso, é só um 
exemplo). Uma das soluções desenvolvida 
e em produção calcula o preço pago por 
cada cliente de acordo com o número de 
requisições executadas no servidor ao 
mês. Crie um programa que calcule o 
valor pago por cada cliente mensalmente, 
de acordo com o número de requisições 
realizadas. Uma outra informação é que 
há um desconto de 10% no valor total 
quando as requisições ultrapassam o valor 
de 10.000 requisições ao mês. Considere 
ainda que o cliente deve pagar R$ 1,15 a 
cada consulta. 
*/
#define PRECO_P_ACESSO 2 //Preço por acesso R$2 

int main(){
  char nome[50], cpf[14];
  int age, req_mes, consultas;
  float preco;
  printf("Olá, bom dia! Seja bem-vindo(a)!\nPara melhor experiência do Usuário, conceda-nos algumas de suas informações.\n");
  printf("Seu Nome: ");
  scanf("%s", &nome);
  printf("Sua Idade: ");
  scanf("%i", &age);
  printf("Seu CPF(com ponto/traço): ");
  scanf("%s", &cpf);
  printf("Muito Bom!\nAgora dados do tráfego do mês.\nRequisições deste mês: ");
  scanf("%i", &req_mes);
  printf("Quantas consultas esse mês");
  scanf("%i", &consultas);
  printf("Saldo\n--------------------------------------\n%s\n%i anos\nCPF: %s\n--------------------------------------\n", nome, age, cpf);
  if (req_mes < 10000) {
    preco = req_mes * PRECO_P_ACESSO + consultas * 1.15 +1.15;
    printf("Tráfego %i/mês * R$2.00\nConsultas %i/mês * 1.15\n--------------------------------------\nA pagar: R$%f", req_mes, consultas, preco);
    return 0;
  }
  preco = req_mes * PRECO_P_ACESSO * 0.9 + consultas * 1.15 +1.15;
  printf("Tráfego %i/mês * R$2.00 -10%%\nConsultas %i/mês * 1.15\n--------------------------------------\nA pagar: R$%f", req_mes, consultas, preco);
  return 0;
}