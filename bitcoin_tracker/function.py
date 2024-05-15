from frames import *
import requests

# Função para puxar os dados ---------------------------------------------------------------------

def info():
    api_link = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CGBP%2CBRL'

    # Requisição HTTP ---------------------------------------------------------------------

    response = requests.get(api_link)

    # Convertendo os dados para dicionário ---------------------------------------------------------------------

    dados = response.json()

    # Valor em Dollar ---------------------------------------------------------------------

    valor_usd = float(dados['USD'])
    valor_formatado_usd = '$ {:_.2f}'.format(valor_usd)
    valor_formatado_usd = valor_formatado_usd.replace('.',',').replace('_','.')
    l_dollar['text'] = valor_formatado_usd

    # Valor em Real ---------------------------------------------------------------------

    valor_brl = float(dados['BRL'])
    valor_formatado_brl = '{:_.2f}'.format(valor_brl)
    valor_formatado_brl = valor_formatado_brl.replace('.',',').replace('_','.')
    l_reais['text'] = 'Em Real: R$ '+valor_formatado_brl

    # Valor em Euro ---------------------------------------------------------------------

    valor_eur = float(dados['EUR'])
    valor_formatado_eur = '{:_.2f}'.format(valor_eur)
    valor_formatado_eur = valor_formatado_eur.replace('.',',').replace('_','.')
    l_euro['text'] = 'Em Euro: € '+valor_formatado_eur

    # Valor em Libra ---------------------------------------------------------------------

    valor_lbr = float(dados['GBP'])
    valor_formatado_lbr = '{:_.2f}'.format(valor_lbr)
    valor_formatado_lbr = valor_formatado_lbr.replace('.',',').replace('_','.')
    l_libra['text'] = 'Em Libra: £ '+valor_formatado_lbr

    frame_baixo.after(1000, info)
