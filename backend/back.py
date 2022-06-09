# Backend do tomasulo, lendo e despachando as intruções

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
        return f"{self.ciclosNecessarios}: {self.instrucao}, {self.rdest}, {self.rsrc1}, {self.rsrc2}"
        
    def __repr__(self) -> str:
        return f"{self.ciclosNecessarios}: {self.instrucao}, {self.rdest}, {self.rsrc1}, {self.rsrc2}"
class Back:
    instrucoesDisco: str
    
    def __init__(self, path) -> None:
        self.instrucoesDisco = []
        
        with open(path) as file:
            for linha in file:
                linha = linha.strip()
                
                # Remover comentários e espaços em branco
                if not linha.startswith('#') and not linha == '':
                    self.instrucoesDisco.append(linha)
            
    def parseInstrucoes(self):
        # Salvando em uma classe propria para a instrução
        self.instrucoes = []
        
        for instrucao in self.instrucoesDisco:
            parseInst = instrucao.split(':')
            
            # Separando número de ciclos da instrucao
            ciclos = parseInst[0].strip()
            i      = parseInst[1].strip()
            
            parseIntruction = Instrucao()
            parseIntruction.ciclosNecessarios = ciclos
            parseIntruction.instrucao = i[0].strip()
            parseIntruction.rdest = i[1].strip()
            parseIntruction.rsrc1 = i[2].strip
            
            # Adicionando o segundo registrador para instruções que precisam de 2 registradores
            # de origem 
            if len(i) == 4:
                parseIntruction.rsrc2 = i[3].strip()
                
            self.instrucoes.append(parseIntruction)
        
    def printInstrucoes(self):
        print(self.instrucoes[0])