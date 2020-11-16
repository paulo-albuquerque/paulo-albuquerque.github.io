#1: Primeiro e Segundo nome.
print("""-
Primeiro e Segundo nome.
""")
nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu segundo nome: ")
print("{}, {}." .format(sobrenome, nome))

#2: Calcular a Idade.
print("""-
Calcular a Idade.
""")
import datetime
agora = datetime.datetime.now()
nasceu_em = int(input("Digite o ano que você nasceu: "))
idade = int(agora.year) - nasceu_em
print("Sua idade é {} (caso o dia do seu aniversário já tenha passado)" .format(int(idade)))

#3: Média das notas.
print("""-
Média das notas.
""")
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
n3 = float(input("Digite sua terceita nota: "))
media = (n1 + n2 + n3) / 3
print("Sua média nessa disciplina é {}" .format(float(media)))

#4: R$/hora.
print("""-
Total recebido por hora.
""")
salario = int(input("Digite quanto você recebe por mês (R$): "))
horas_diarias = int(input("Digite quantas horas você trabalha por dia: "))
horas_mensais = horas_diarias * 30
por_hora = salario / horas_mensais
print("Considerando um mês de 30 dias, você recebe R$ {} por hora" .format(por_hora))

#5: R$ x m²
print("""-
Total gasto por m².
""")
comprimento = int(input("Digite o comprimento do terreno (em metros): "))
largura = int(input("Digite a largura do terreno (em metros): "))
area = comprimento * largura
custo_total = area * 850
print("Para um terreno de {} m², a custo total será de R$ {}" .format(area, custo_total))

#6: Função quadrática.
print("""-
Equação do segundo grau.
""")
import math
print("""Para um equação de segundo grau (função quadrática) temos o padrão de
ax² + bx + c onde a, b e c são números reais e a ≠ 0, 
sabendo disso:
""")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
if a == 0:
    print("A valor informado para o coeficiente a é inválido")
else:
    delta = (b**2) - (4*a*c) #Delta
    if delta < 0:
        print("Equação não possui raízes reais")
    elif delta == 0:
        raiz = (-b-math.sqrt(delta)) / (2*a) #x
        print("A equação só possui uma raiz (ou duas raizes iguais): {}" .format(raiz))
    else:
        raiz1 = (-b+math.sqrt(delta)) / (2*a) #x'
        raiz2 = (-b-math.sqrt(delta)) / (2*a) #x''
    print("As duas raízes da equação ({})x² + ({})x + ({}) são {} e {}" .format(a, b ,c, raiz1, raiz2))

#7: Verdadeiro ou Falso
print("""-
Joguinho do verdadeiro ou falso.
""")
q1 = input(""""O Brasil é o país mais populoso do mundo."
Isso é: """)
q2 = input(""""2+2*2 = 6"
Isso é: """)
q3 = input(""""Programar é divertido."
Isso é: """)
print("""Gabarito: falso, verdadeiro, verdadeiro
Suas respostas: {}, {}, {}""" .format(q1, q2, q3))

#8: Loja.
print("""-
Desconto da loja.
""")
p1 = int(input("Digite o preço do primeiro produto: "))
p2 = int(input("Digite o preço do segundo produto: "))
p3 = int(input("Digite o preço do terceiro produto: "))
total = p1 + p2 + p3
off = total * 0.20
novo_total = total - off
print("""O total das compras foi {} reais.
O disconto foi de {} reais.
O cliente deve pagar {} reais.""" .format(total, int(off), int(novo_total)))

#9: Temperaturas
print("""-
Conversor de temperaturas.
""")
c = float(input("Digite a temperatura em Celsius: "))
c_k = c + 273.15
c_f = (c * 1.8) + 32
print("""
Temperatura em Celsius: {}
Temperatura em Kelvin: {}
Temperatura em Fahrenheit: {}""" .format(c , c_k, c_f))

#10: Passos.
print("""-
Quilômetros para passos (sendo um passo = 0,82m)
""")
km = float(input("Digite uma distância em Quilômetros (Km): "))
km_para_m = km * 1000
m_para_passos = km_para_m / 0.82
print("{} quilômetros equivalem a {} passos." .format(km, int(m_para_passos)))

#11 Horas por pedreiro.
print("""-
Em quanto tempo x pedreiros vão terminar o muro (sabendo que 8 terminam em 72 horas).
""")
h_com_8p = 72
h_com_1p = 72*8                    #8p=72 // 4p=144h // 2p=288h // 1p=576
np = int(input("Digite o número total de pedreiros: "))
h_com_np = h_com_1p / np
print("{} pedreiros terminarão o muro em {} horas" .format(np, h_com_np))

#12: Passagens.
print("""-
Relação de passageiros.
""")
passagem = 30
estudante_passagem = passagem / 2
porcentagem_normal = 0.55
porcentagem_estudantes = 0.45
total_por_dia = int(input("Digite o total que a empresa acumulou em um dia (R$): "))
passageiros = total_por_dia / passagem
passageiros_normais = passageiros * porcentagem_normal
estudantes = (passageiros * porcentagem_estudantes) * 2
print("Foram {} pagantes normais e {} estudantes." .format(int(passageiros_normais), int(estudantes)))