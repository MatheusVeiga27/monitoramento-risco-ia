#Programa de Sistema de Monitoramento de Risco Ético no Uso de IA
n = int(input("Quantas atividades são?:" )) 
i = 0
high_risk = 0
show_not = 0
uso_list= []
tipo_list = []
nota_list = []

while (i!=n):
  uso = int(input("Usou IA? 1- Sim 0- Não"))
  uso_list.append(uso)
  if uso == 1:
    tipo = int(input("Qual o tipo? 1- Pesquisa 2- Geração de Texto 3- Geração de Código"))
    tipo_list.append(tipo)
    show = int(input("Declarou o uso? 1- Sim 0-Não"))
    if show == 0:
      show_not = show_not + 1
    nota = int(input("Nota da atividade:"))
    nota_list.append(nota)
    if show == 0 and nota >=80:
        high_risk = high_risk + 1
  else:
    nota = int(input())
    nota_list.append(nota)
  i = i + 1

if n > 0:
    uso_soma = sum(uso_list)
    uso_fracao = (uso_soma / n) * 100
    print(f"Percentual de uso de IA:{uso_fracao:.2f}%")

    high_risk_fraction = (high_risk / n) * 100
    print(f"Percentual de alto risco ético:{high_risk_fraction:.2f}%")

    nota_soma = sum(nota_list)
    nota_fraction = nota_soma / n
    print(f"Média geral da turma:{nota_fraction:.2f}")

    print(f"Atividades com IA não declarada:{show_not}")

    if  high_risk_fraction>= 30:
        print("Classificação da turma: Risco Ético Elevado")
    elif high_risk_fraction < 30 and high_risk_fraction >= 10:
        print("Classificação da turma: Risco Ético Moderado")
    else:
        print("Classificação da turma: Risco Ético Baixo")

print("Encerrando")