import os
from frontend import front

pwd = os.getcwd()
menu_principal = front.Tela(pwd+'/assets/instrucoes.txt')
menu_principal.desenharTela()