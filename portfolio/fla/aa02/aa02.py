#1: Maior de idade.
print("""-
Maior ou menor de idade.
""")
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você não é maior de idade.")

#2: Média.
print("""-
Calcular a média da disciplina.
""")
print("""Observe que este programa apenas calcula as notas em uma escala de 0 a 10.
Caso queira calcular sua nota em uma escala de 0 a 100, mova a casa decimal 1 vez
para a esquerda e insira no console o novo valor.
""")
n1 = float(input("Digite sua primeira nota (ex: 7.0): "))
n2 = float(input("Digite sua segunda nota (ex: 8.0): "))
media = (n1 + n2) / 2
if media < 0:
    print("Ocorreu um erro ao calcular a média. Verifique os valores de suas notas e tente novamente.")
elif media > 10:
    print("Ocorreu um erro ao calcular a média. Verifique os valores de suas notas e tente novamente.")
else:
    print("Sua média foi {}" .format(media))
    if media >= 7:
        print("Parabéns! Você foi aprovado.")
    else:
        print("Você não foi aprovado.")

#3: Saudação.
print("""-
Saudação do dia.
""")
nome = input("Digite seu nome: ")
sexo = input("Informe com 1 letra o seu sexo (f para \"feminino\", m para \"masculino\"): ")
if sexo == "f":
    print("Bom dia senhora {}." .format(nome))
elif sexo == "m":
    print("Bom dia senhor {}." .format(nome))

#4: Par ou ímpar.
print("""-
Digite um número e descubra se ele é par ou ímpar.
""")
n = int(input("Digite um número: "))
if n % 2 == 0:
    print("{} é par." .format(n))
else:
    print("{} é ímpar." .format(n))

#5: Triângulos.
print("""-
Descobrindo a classificação de um triângulo.
""")
l1 = float(input("Informe o tamanho de um dos lados do triângulo: "))
l2 = float(input("Informe o tamanho de outro lado do triângulo: "))
l3 = float(input("Informe o tamanho do último lado do triângulo: "))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l3:
    if l1 == l2 and l2 == l3:
        print("Trata-se de um triângulo \"Equilátero\".")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Trata-se de um triângulo \"Isóceles\".")
    else:
        print("Trata-se de um triângulo \"Escaleno\".")
else:
    print("Não trata-se de um triângulo.")
    
#6: IMC
print("""-
Cálculo do seu Índice de Massa Corporal (para adultos).
""")
peso = float(input("Informe seu peso em Kg (Ex.: 60.0): "))
altura = float(input("Informe sua altura em metros (Ex.: 1.73): "))
imc = peso / (altura ** 2)
print("Seu IMC é {}" .format(imc))
if imc < 17:
    print("Muito abaixo do peso.")
elif 17 < imc <= 18.49:
    print("Abaixo do peso.")
elif 18.5 < imc <= 24.99:
    print("Peso normal.")
elif 25 < imc <= 29.99:
    print("Acima do peso.")
elif 30 < imc <= 34.99:
    print("Obesidade I")
elif 35 < imc <= 39.99:
    print("Obesidade II (Severa).")
elif imc > 40:
    print("Obesidade III (Mórbida).")

#7: Km/litro.
print("""-
Cálculo de quilômetros por litro.
""")
km_l = int(input("Quantos quilômetros o carro faz por litro? "))
l_atual = int(input("Quantos litros o carro possui atualemente? "))
km_a_percorrer = int(input("Quantos quilômetros você deseja percorrer com o carro? "))
l_necessario = km_a_percorrer - (l_atual * km_l)
l_a_abastecer = l_necessario - l_atual
if l_a_abastecer <= 0:
    print("Você não necessita reabastecer.")
else:
    print("Você necessita abastercer {} litros." .format(l_a_abastecer))
    
#8: Doar Sangue.
print("""-
Requisitos para a doação de sangue.
""")
def nao_qualificado():
    print("Infelizmente você não pode ser doador.")
idade_necessaria = int(input("Qual a sua idade? "))
if 19 <= idade_necessaria <= 69:
    peso_necessario = float(input("Qual o seu peso: "))
    if peso_necessario >= 59:
        tatuagem = input("""Você fez alguma tatuagem no último ano.
        (VERDADEIRO OU FALSO): """)
        if tatuagem == "FALSO":
            alcool = input("""Você ingeriu álcool nas últimas 12 horas.
            (VERDADEIRO OU FALSO): """)
            if alcool == "FALSO":
                print("Parabéns, você pode doar sangue.")
            else:
                nao_qualificado()
        else:
            nao_qualificado()
    else:
         nao_qualificado()
else:
    nao_qualificado()

#9: Multa.
print("""-
Cálculo da multa.
""")
v_max = int(input("Informe a velocidade máxima permitida: "))
v_registrada = int(input("Informe a velocidade do motorista: "))
if v_registrada <= v_max:
    print("Não precisa pagar multa.")
elif v_registrada <= v_max * 1.20:
    print("(Infração Média) Multa de 85 reais.")
elif v_max * 1.20 < v_registrada <= v_max * 1.50 :
    print("(Infração grave) Multa de 127 reais.")
elif v_registrada > v_max * 1.50:
    print("(Infração gravíssima) Multa de 574 reais.")

#10: Número-Mês
print("""-
Converta um número para um mês
""")
def um():
    return "Janeiro"
def dois():
    return "Fevereiro"
def tres():
    return "Março"
def quatro():
    return "Abril"
def cinco():
    return "Maio"
def seis():
    return "Junho"
def sete():
    return "Julho"
def oito():
    return "Agosto"
def nove():
    return "Setembro"
def dez():
    return "Outubro"
def onze():
    return "Novembro"
def doze():
    return "Dezembro"
meses = {1:um, 2:dois, 3:tres, 4:quatro, 5:cinco, 6:seis, 7:sete, 8:oito, 9:nove, 10:dez, 11:onze, 12:doze}
print(meses.get(int(input("Digite um número: ")))())

#11: Crescente.
print("""-
Organizar números em ordem crescente
""")
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))
if str(x) < str(y) < str(z):
    print(str(x)+", "+str(y)+", "+str(z))
elif str(x) < str(z) < str(y):
    print(str(x)+", "+str(z)+", "+str(y))
elif str(y) < str(x) < str(z):
    print(str(y)+", "+str(x)+", "+str(z))    
elif str(y) < str(z) < str(x):
    print(str(y)+", "+str(z)+", "+str(x))
elif str(z) < str(x) < str(y):
    print(str(z)+", "+str(x)+", "+str(y))
elif str(z) < str(y) < str(x):
    print(str(z)+", "+str(y)+", "+str(x))

#12: Datas.
print("""-
Organizar datas em ordem crescente.
""")
d1 = int(input("Digite o dia da primeira data: "))
m1 = int(input("Digite o mês da primeira data: "))
y1 = int(input("Digite o ano da primeira data: "))
soma1 = d1 + (m1 * 30) + (y1 * 365)

d2 = int(input("Digite o dia da segunda data: "))
m2 = int(input("Digite o mês da segunda data: "))
y2 = int(input("Digite o ano da segunda data: "))
soma2 = d2 + (m2 * 30) + (y2 * 365)
if soma1 < soma2:
    print("{}/{}/{}, {}/{}/{}" .format(d1, m1, y1, d2, m2, y2))
else:
    print("{}/{}/{}, {}/{}/{}" .format(d2, m2, y2, d1, m1, y1,))

#13: Cálculo de gastos.
print("""-
Calcula gastos da noite.
""")
beber = input("Você planeja beber. (VERDADEIRO OU FALSO): ")
comer = input("Você planeja comer. (VERDADEIRO OU FALSO): ")
transporte = input("Você planeja contratar transporte. (VERDADEIRO OU FALSO): ")
qnt_pessoas = int(input("Quantas pessoas sairão hoje a noite (incluindo você): "))
if beber == "VERDADEIRO":
    total_bebidas = qnt_pessoas * 80
else:
    total_bebidas = 0
if comer == "VERDADEIRO":
    total_comida = qnt_pessoas * 60
else:
    total_comida = 0
if transporte == "VERDADEIRO":
    total_transporte = qnt_pessoas * 15
else:
    total_transporte = 0
total_noite = total_bebidas + total_comida + total_transporte
print("O gasto estimado desta noite será de {} reais." .format(total_noite))

#14: Aposentadoria.
print("""-
Cálculo do benefício da previdência.
""")
sexo_inss = input("Qual seu sexo (M/F)? ")
idade_inss = int(input("Com quantos anos você começou a contribuir? "))
if sexo_inss == "M":
    idm = 65
    print("Você só terá direito a se aposentar com {} anos." .format(idm))
else:
    idm = 62
    print("Você só terá direito a se aposentar com {} anos." .format(idm))
idm_b = idm - idade_inss
if 25 <= idm_b < 30:
    print("Com essa idade você terá direito a 70% do benefício.")
elif 30 <= idm_b < 35:
    print("Com essa idade você terá direito a 77.5% do benefício.")
elif 35 <= idm_b < 40:
    print("Com essa idade você terá direito a 87.5% do benefício.")
elif idm_b >= 40:
    print("Com essa idade você terá direito a 100% do benefício.")
else:
    print("Ocorreu um erro ao calcular a porcentagem do seu benefício ou pode ser que você não tenha direito a recebê-lo.")
if idade_inss + 40 <= idm_b:
    idm100 = idm_b
else:    
    idm100 = idade_inss + 40
print("Você precisa trabalhar até os {} anos para ter direito a 100% do benefício." .format(idm100))

#15: Média.
print("""-
Cálculo da média.
""")
n1 = int(input("Informe a primeira nota: "))
n2 = int(input("Informe a segunda nota: "))
n3 = int(input("Informe a terceira nota: "))
media = (n1 + n2 + n3) / 3
print("Sua média foi {}" .format(media))
if media < 4:
    print("Você foi reprovado")
elif media >= 7:
    print("Você foi aprovado.")
elif 4 <= media < 7:
    nota_final = (5 - media * 0.6 ) / 0.4
    print("Você precisa de {}" .format(nota_final))

##