import os
from frontend import front

menu_principal = front.Tela(os.getcwd()+'/assets/instrucoes.txt')
menu_principal.desenharTela()