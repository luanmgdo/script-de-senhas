import time
import secrets
import string
from random import *

def criar_senha():
    tamanho_da_senha = randint(10,14)
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for i in range(tamanho_da_senha))
    senha_existe = verificar_senha(senha)
    if(senha_existe):
        print("senha ja existente, por favor execute novamente para criar outra senha")
    else:
        print("senha gerada:", senha)
        salvar_senha(senha)
       

def salvar_senha(senha):
    print("salvando senha no arquivo")
    db = open("database.txt", 'a') #abrir arquivo
    db.write('\n')
    db.write(senha)
    db.close() #fechar arquivo


def verificar_senha(senha):
    senha_existe = False
    db = open("database.txt", 'r') #abrir arquivo
    lines = db.readlines()
    for line in lines:
        line = line.strip()
        if(senha == line):
            senha_existe = True
    db.close() #fechar arquivo        
    return senha_existe

print("1 para criar nova senha | 2 para verificar se senha existe")
escolha = input("O que deseja fazer?: ")

if(escolha == '1'):
    criar_senha()
if(escolha == '2'):
    senha = input("digite a senha que deseja verificar: ")
    senha_existe = verificar_senha(senha)
    if(senha_existe):
        print("A sua senha ja existe no arquivo")
    else:
        novo = input("A senha não existe no arquivo, deseja salva-la?\n")
        if(novo == 'sim' or novo == 'Sim' or novo == 'S' or novo == 's'):
            salvar_senha(senha)
        else:
            print("encerrando programa")

if(escolha != '1' and escolha != '2'):
    print("escolha nao identificada")