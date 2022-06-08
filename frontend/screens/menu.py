import PySimpleGUI as sg 
from frontend.models import text_front, keys_front

# Layout que será usado na aplicação principal
class LayoutMenu:      
    def __init__(self) -> None:
        self.pipeline_layout = [
            sg.Button(text_front.PIPELINE_BUTTON1_TEXT, key=keys_front.PIPELINE_BUTTON1_KEY, disabled=True), 
            sg.Button(text_front.PIPELINE_BUTTON2_TEXT, key=keys_front.PIPELINE_BUTTON2_KEY, disabled=True),
            sg.Button(text_front.PIPELINE_BUTTON3_TEXT, key=keys_front.PIPELINE_BUTTON3_KEY, disabled=True),
            sg.Button(text_front.PIPELINE_BUTTON4_TEXT, key=keys_front.PIPELINE_BUTTON4_KEY, disabled=True),
            sg.Button(text_front.PIPELINE_BUTTON5_TEXT, key=keys_front.PIPELINE_BUTTON5_KEY, disabled=True),
            sg.Button(text_front.PIPELINE_BUTTON6_TEXT, key=keys_front.PIPELINE_BUTTON6_KEY, disabled=True),
            sg.Button(text_front.PIPELINE_BUTTON7_TEXT, key=keys_front.PIPELINE_BUTTON7_KEY, disabled=True),
            sg.Button(text_front.PIPELINE_BUTTON8_TEXT, key=keys_front.PIPELINE_BUTTON8_KEY, disabled=True)
            ]
        
        self.banco_registradores = [
            [text_front.BANCO_REGISTRADOR_BUTTON1_TEXT],
            [text_front.BANCO_REGISTRADOR_BUTTON2_TEXT],
            [text_front.BANCO_REGISTRADOR_BUTTON3_TEXT],
            [text_front.BANCO_REGISTRADOR_BUTTON4_TEXT],
            [text_front.BANCO_REGISTRADOR_BUTTON5_TEXT],
            [text_front.BANCO_REGISTRADOR_BUTTON6_TEXT],
            [text_front.BANCO_REGISTRADOR_BUTTON7_TEXT],
            [text_front.BANCO_REGISTRADOR_BUTTON8_TEXT],
        ]
        
        self.layout = [
            [sg.Button(text_front.CLOCK_BUTTON_TEXT, key=keys_front.CLOCK_BUTTON_KEY), sg.VSeparator(), sg.vtop(sg.Table(self.banco_registradores, size=(30,8), auto_size_columns=False, hide_vertical_scroll=True, justification='c', key=keys_front.SELECTED_BANCO_REGISTRADOR_KEY))],
            [sg.vtop(self.pipeline_layout)]
        ]