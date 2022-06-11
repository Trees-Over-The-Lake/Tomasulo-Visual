# Célula que armazena uma instrução

class Instrucao:
    ciclosNecessarios: int
    instrucao: str
    rsrc1: str
    rsrc2: str
    rdest: str
    
    def __init__(self) -> None:
        self.ciclosNecessarios = 0
        self.instrucao = ''
        self.rdest = ''
        self.rsrc1 = ''
        self.rsrc2 = ''

    def __str__(self) -> str:
        if self.rsrc2 == '':
            return f"{self.ciclosNecessarios}: {self.instrucao}, {self.rdest}, {self.rsrc1}"
        else:     
            return f"{self.ciclosNecessarios}: {self.instrucao}, {self.rdest}, {self.rsrc1}, {self.rsrc2}"
        
    def __repr__(self) -> str:
        if self.rsrc2 == '':
            return f"({self.ciclosNecessarios}: {self.instrucao}, {self.rdest}, {self.rsrc1})"
        else:     
            return f"({self.ciclosNecessarios}: {self.instrucao}, {self.rdest}, {self.rsrc1}, {self.rsrc2})"
    
    # Get instruções para exibir na tela
    def getInstr(self):
        if self.rsrc2 == '':
            return f"{self.instrucao}, {self.rdest}, {self.rsrc1}"
        else:     
            return f"{self.instrucao}, {self.rdest}, {self.rsrc1}, {self.rsrc2}" 