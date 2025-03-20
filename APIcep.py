import requests
import json
import pandas as pd
import unicodedata

UF_VALIDAS = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT",
    "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO",
    "RR", "SC", "SP", "SE", "TO"
]

def remover_acentos(texto):
    # Vou remover acentos especiais
    return ''.join(c for c in unicodedata.normalize('NFKD', texto) if not unicodedata.combining(c))

def buscar_cep(cep):
    cep = cep.replace("-", "").replace(".", "").strip()
    
    if len(cep) == 8 and cep.isdigit():
        link = f"https://viacep.com.br/ws/{cep}/json/"
        try:
            resposta = requests.get(link, timeout=5)
            resposta.raise_for_status()

            dados = resposta.json()        
            if "erro" not in dados:
                print("\n🔹 Dados do CEP: ")
                print(f"CEP: {dados['cep']} ")
                print(f"Estado: {dados['uf']} ")
                print(f"Cidade: {dados['localidade']} ")
                print(f"Bairro: {dados['bairro']} ")
                print(f"Logradouro: {dados['logradouro']} ")
            else:
                print("❌ CEP não encontrado.")
        except requests.exceptions.RequestException:
            print("❌ Erro de conexao. Por favor, verifique sua internet.")
    else:
        print("❌ CEP inválido. Digite apenas 8 números.")


def buscar_endereco(uf:str, cidade:str, endereco:str):
    uf = uf.upper().strip()

    if uf not in UF_VALIDAS:
        print(f"❌ UF inválida. Digite um estado válido (exemplo: SP, RJ, MG).")
        return
    
    cidade = remover_acentos(cidade.strip())
    endereco = remover_acentos(endereco.strip())

    link = f"https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/"
    try:
        resposta = requests.get(link, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()

        if isinstance(dados, list) and len(dados) > 0:
            print(f"\n 🔹 Endereços encontrados: ")

            tabela = pd.DataFrame(dados)
            print(tabela[["cep", "logradouro", "bairro", "localidade", "uf"]])
        else:
            print("❌ Nenhum endereço encontrado.")
    except requests.exceptions.RequestException:
        print("❌ Erro de conexão.")

while True:
    print(f"\n {'-' * 10} 🔍 Buscador de CEP e Endereço {'-' * 10} ".center(50))
    escolha = input("""\nDeseja buscar por:
    [1] - CEP
    [2] - Endereço
    [3] - Sair\n
(Digite sua resposta númerica): """)

    if escolha == "1":
        cep = input("Digite seu CEP: ")
        buscar_cep(cep)
    elif escolha == "2":
        uf = input("(exemplo: SP, RJ)\nUF: ").strip().upper()
        cidade = input("Cidade: ").strip()
        endereco = input("Endereço (logradouro): ").strip()
        buscar_endereco(uf, cidade, endereco)
    elif escolha == '3':
        print(f" {'=-' * 5} PROGRAMA ENCERRADO {'=-' * 5} ".center(50))
        break
    else:
        print("❌ Opção inválida.")

