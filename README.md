# Buscador de CEP e Endereço

Este projeto em Python permite realizar buscas de CEP e Endereços utilizando a API pública do [ViaCEP](https://viacep.com.br). Ele oferece a funcionalidade de buscar dados a partir de um CEP ou realizar uma busca por estado, cidade e endereço (logradouro).

## Funcionalidades

- **Buscar CEP:** Ao fornecer um CEP válido, o programa retorna as informações sobre o endereço, como cidade, estado, bairro e logradouro.
- **Buscar Endereço:** Ao fornecer o estado (UF), cidade e logradouro, o programa retorna uma lista de endereços encontrados, com o respectivo CEP.

## Tecnologias Utilizadas

- **Python 3.13**
- **Bibliotecas:** 
  - `requests`: Para fazer as requisições HTTP à API do ViaCEP.
  - `pandas`: Para organizar e exibir os dados de forma tabular.
  - `unicodedata`: Para remover acentos dos textos de entrada.

## Como Usar

1. Clone ou faça o download deste repositório para sua máquina local.

```bash
git clone https://github.com/SabrinaGamaa/Cep.git

