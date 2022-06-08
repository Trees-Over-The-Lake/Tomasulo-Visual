import PySimpleGUI as sg

from frontend.screens import menu
from frontend.models import text_front
from backend import back

# Classe que desenha a GUI na tela
class Tela:
    _window: sg.Window
    backend: back.Back
    
    def __init__(self, instructions_path) -> None:
        self.layout_menu = menu.LayoutMenu().layout 
    
        self.backend = back.Back(instructions_path)
        self.backend.printInstucoes()
        
    # Desenhando a tela para o usuário
    def desenharTela(self) -> None:
        
        self._window = sg.Window(text_front.FRONT_TITLE_WINDOW_TEXT, self.layout_menu, resizable=True, font='Helvetica 14')
        
        while True:
            event, values = self._window.read()
            
            if event == sg.WIN_CLOSED:
                break
            
            print(values)
            
    # Fechando a janela
    def close(self) -> None:
        self._window.close()