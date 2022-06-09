# Backend do tomasulo, lendo e despachando as intruções

class Instrucao:
    ciclosNecessarios: int
    instrucao: str
    rsrc1: str
    rsrc2: str
    rdest: str

    def __str__(self) -> str:
        print(f"Ciclos necessários: {self.ciclosNecessarios}: {self.instrucao}, {self.rdest}, {self.rsrc1}, {self.rsrc2}")
class Back:
    instrucoes: str
    
    def __init__(self, path) -> None:
        self.instrucoes = []
        
        with open(path) as file:
            for linha in file:
                linha = linha.strip()
                
                # Remover comentários e espaços em branco
                if not linha.startswith('#') and not linha == '':
                    self.instrucoes.append(linha)
            
    def printInstucoes(self):
        print(self.instrucoes)
        
    def parseInstrucoes(self):
        for instrucao in self.instrucoes:
            pass