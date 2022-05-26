import PySimpleGUI as sg
from frontend.screens import menu
from frontend.models import text_front

# Classe que desenha a GUI na tela
class Tela:
    _window: sg.Window
    
    def __init__(self) -> None:
        self.layout_menu = menu.LayoutMenu().layout    
    
    # Desenhando a tela para o usuário
    def desenharTela(self) -> None:
        
        self._window = sg.Window(text_front.FRONT_TITLE_WINDOW_TEXT, self.layout_menu, resizable=True)
        
        while True:
            event, values = self._window.read()
            
            if event == sg.WIN_CLOSED:
                break
            
    # Fechando a janela
    def close(self) -> None:
        self._window.close()