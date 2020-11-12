# funções declaradas
def media (nota1, nota2, nota3):
    return ((nota1 + nota2 + nota3)/3)

def media_aproveitamento (nota1, nota2, nota3):
    return((nota1 + nota2 * 2 + nota3 * 3 + media(nota1, nota2, nota3) )/7)

def conceito (ma):
    if (ma >= 9):
        return "A"
    elif (ma >=7.5):
        return "B"
    elif (ma >=6):
        return "C"
    elif (ma >=4):
        return "D"
    else:
        return "E"
        
def mensagem (con):
    if (con == "A" or con == "B" or con == "C"):
        return "APROVADO"
    else:
        return "REPROVADO"

# variáveis de entrada
aluno = int(input('Digite a matrícula do aluno: '))
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))

# variáveis chamando funções para facilitar na manipulação das menssagens
ma = media_aproveitamento(nota1, nota2, nota3)
con = conceito(ma)
msg = mensagem(con)

# dados de saída
print('-------------------------------------')
print('O Aluno:', aluno ,'obteve as notas:')
print(nota1)
print(nota2)
print(nota3)
print('Média: ', media(nota1, nota2, nota3))
print('Média de Aproveitamento: ',ma)
print('Conceito: ',con)
print("Aluno ",msg)