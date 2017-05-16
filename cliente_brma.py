#!/bin/python3
#Cliente BRMA escrito em python3.
#TODO: Implementar a criptografia do applet: CryptP.class
#Inserir endereço do servidor, usuário e senha
#victor.oliveira@gmx.com

from urllib.request import urlopen
from urllib.parse import urlencode
from telnetlib import Telnet
from time import sleep

server = 'INSERIR ENDEREÇO IP'
usuario = 'INSERIR USUÁRIO'
senha = 'INSERIR SENHA'

def login():
    url = 'http://{}:10001/cgi/loginaux.cgi'.format(server, porta)

    post = {'acao' : 'login',
            'CRYPT' : '0',
            'USERNAME' : usuario,
            'PASSWORD' : senha}
    post = urlencode(post).encode()
    req = urlopen(url, post)
    print('Conectado.')

def keep_alive():
    while True:
        print('Autenticando...')
        tn = Telnet(server, 10002)
        tn.write(usuario.encode() + b'\n' + senha.encode() + b'\n')
        print('Autenticado.')
        print(tn.read_all().decode())
        tn.close()
        sleep(480)

login()
keep_alive()
