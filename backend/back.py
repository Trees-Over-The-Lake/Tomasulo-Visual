# Backend do tomasulo, lendo e despachando as intruções

class Back:
    instrucoes: str
    
    def __init__(self, path) -> None:
        self.instrucoes = ''
        
        with open(path) as file:
            self.instrucoes += file.read()
        
    def printInstucoes(self):
        print(self.instrucoes)