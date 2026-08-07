import json
from xml.etree.ElementTree import indent


def carregar_alunos():
    try:
        arquivo = open("alunos.json", encoding="utf-8")
        alunos = json.load(arquivo)
        arquivo.close()
        return alunos
    except FileNotFoundError:
        arquivo = open("alunos.json", encoding="utf-8", mode="w")
        json.dump([], arquivo)
        arquivo.close()
        return []

def salvar_alunos(lista):
    arquivo = open("alunos.json", encoding="utf-8", mode='w')
    json.dump(lista, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()