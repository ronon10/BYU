import csv

def limpar_inumber(inumber):
    inumber_limpo = inumber.replace("-", "") 
    if not inumber_limpo.isdigit():
        return "Invalid I-Number" 
    if len(inumber_limpo) < 9:
        return "Invalid I-Number: too few digits" 
    if len(inumber_limpo) > 9:
        return "Invalid I-Number: too many digits"
    return inumber_limpo


def buscar_aluno_por_inumber():

    with open('C:/Users/realves/Documents/BYU/CSE111/week 5/students.csv', 'r') as arquivo:
        linhas = arquivo.readlines()[1:]
        dicionario_alunos = {}
        
        for linha in linhas:
            dados = linha.strip().split(",")
            inumber = dados[0]
            nome = dados[1]
            dicionario_alunos[inumber] = nome
    

    inumber_usuario = input("Digite o I-Number do aluno: ")
    inumber_usuario_limpo = limpar_inumber(inumber_usuario)
    

    if "Invalid" in inumber_usuario_limpo:
        print(inumber_usuario_limpo)
    else:
 
        nome_aluno = dicionario_alunos.get(inumber_usuario_limpo, "Nenhum aluno")
        print(nome_aluno)

buscar_aluno_por_inumber()
