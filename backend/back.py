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
            
class Back:
    instrucoesDisco: str
    
    def __init__(self, path) -> None:
        self.instrucoesDisco = []
        
        # Abrindo arquivo no disco e lendo as instruções
        with open(path) as file:
            for linha in file:
                linha = linha.strip()
                
                # Remover comentários e espaços em branco
                if not linha.startswith('#') and not linha == '':
                    self.instrucoesDisco.append(linha)
        
        # Fazendo o parse das instruções
        self._parseInstrucoes()
            
    # Lista de instruções e seus tempos de execucao
    def getInstrucoes(self):
        return self._instrucoes
    
    # Pegando tempos de execucao e instrução separadamente
    def getInstrucoesAndCiclos(self):
        return ([x.getInstr() for x in self._instrucoes], [x.ciclosNecessarios for x in self._instrucoes])        
    
    def _parseInstrucoes(self):
        # Salvando em uma classe propria para a instrução
        self._instrucoes  = []
        
        for instrucao in self.instrucoesDisco:
            parseInst = instrucao.split(':')
            
            # Separando número de ciclos da instrucao
            ciclos    = parseInst[0].strip()
            i         = parseInst[1].split(' ')
            
            # Removendo elementos vazios
            i.remove('')
            
            parseIntruction = Instrucao()
            parseIntruction.ciclosNecessarios = ciclos
            parseIntruction.instrucao = i[0].strip()
            parseIntruction.rdest = i[1].strip().replace(',', '')
            parseIntruction.rsrc1 = i[2].strip().replace(',', '')
            
            # Adicionando o segundo registrador para instruções que precisam de 2 registradores
            # de origem 
            if len(i) == 4:
                parseIntruction.rsrc2 = i[3].replace(',', '').strip()
                
            self._instrucoes.append(parseIntruction)
        
    # Printar instruções na tela
    def printInstrucoes(self):
        print(self._instrucoes )