# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 14:12:15 2018

@author: Samsung
"""

# Cria acesso à API do twitter

import tweepy

consumer_key = 'YAIA1fMeeDyTgmo7KZhbddwEj'
consumer_secret = 'hbYm3WXcBokSAKtBCFh25BcawIqIvVSBngx7br96vzs3k7ljBV'
access_token = '943957360351080450-UFrFppfhNb2Bxdps6Vk67BINIRDTuHg'
access_token_secret = 'h9QWCtrVPQkJIDqDb4TpVhDbUOBAy2inUbREfqtclkqom'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Acessa os dados de vários usuário
# Criar uma lista de usuarios e funcao para ver a timeline de cada um deles
perfis_politicos = ['RollembergPSB', 'sinprodf', 'Sindjus', 'sindsepdf']
# perfis_politicos = {"Rollemberg":['RollembergPSB'],"Sind_Professor":['sinprodf'],"Sind_justiça":['Sindjus'], "Sind_DF":['sindsepdf']}

    
def url_compartilhada(usuario_no_twitter):
    linha_tempo = api.user_timeline(usuario_no_twitter)
    return linha_tempo
    
# loop para verificar a timeline de cada usuario 
for perfil in perfis_politicos:
    linha_do_tempo = url_compartilhada(perfil)  
    frase = f'o usuário {perfil} tem a seguinte linha do tempo {linha_do_tempo}'
    print(frase)










