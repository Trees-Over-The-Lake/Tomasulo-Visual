# Backend do tomasulo, lendo e despachando as intruções

from backend.MIPS.instructions import MipsInstructions
from backend.instruction import Instrucao
import enum

class EnumReservationStationStates(enum.Enum):
    SUCCESS = 1
    FULL = 2
    EMPTY = 3

class ReservationStation:
    def __init__(self) -> None:
        self.add_sub = []    # Reserva para 3 instruções simultaneas de add and sub
        self.mul_divide = [] # Reserva para 2 instruções simultaneas de mul e div
        self.load_store = [] # Reserva para 4 instruções simultaneas de load e store
        
        self.instruction_queue = [] # Fila de despacho de instruções
    
    # Todos os gets abaixo estão com valores de tamanho hardcoded
    # Caso queira mudar o tamanho das RS facilmente, só alterar aqui
    def getAddSubReservationSize(self):
        return 3
    
    def getMulDivideReservationSize(self):
        return 2
    
    def getLoadStoreReservationSize(self):
        return 4

    def getInstructionQeueReservationSize(self):
        return 3
    
    def getAddSubList(self):
        return self.add_sub
    
    def getMulDivideList(self):
        return self.mul_divide
    
    def getLoadStoreList(self):
        return self.load_store
    
    def isAddSubEmpty(self):
        return len(self.add_sub) == 0
    
    def isMulDivideEmpty(self):
        return len(self.mul_divide) == 0
    
    def isLoadStoreEmpty(self):
        return len(self.load_store) == 0
    
    def isAllReservationsStationsEmpty(self):
        return self.isAddSubEmpty() and self.isMulDivideEmpty() and self.isLoadStoreEmpty()
    
    def isInstructionQueueFull(self):
        return len(self.instruction_queue) == self.getInstructionQeueReservationSize()
    
    def isInstructionQueueEmpty(self):
        return len(self.instruction_queue) == 0
    
    # Insert a new instruction in the reservation station
    def insertInstruction(self, i: Instrucao):
        # Inserindo na fila de instruções      
        self.instruction_queue.append(i)
        
        # Verificando se ainda há instruções para serem executadas na fila de instruções
        if self.isInstructionQueueEmpty():
           return EnumReservationStationStates.EMPTY    
           
        # Pegando uma nova instrução para ser executada
        execute_inst = self.instruction_queue[0]
        execute_situation = EnumReservationStationStates.FULL # Pré considerando a reserva cheia
        
        if execute_inst.instrucao == MipsInstructions.ADD or execute_inst.instrucao == MipsInstructions.SUB:
            # Considerando que não há RAW ou WAR
            if len(self.add_sub) < self.getAddSubReservationSize():
                self.add_sub.append(ReservationStationCell(execute_inst, True, execute_inst.ciclosNecessarios))
                execute_situation = EnumReservationStationStates.SUCCESS
                            
        
        elif execute_inst.instrucao == MipsInstructions.MUL or execute_inst.instrucao == MipsInstructions.DIV:
            if len(self.mul_divide) < self.getMulDivideReservationSize():
                self.mul_divide.append(ReservationStationCell(execute_inst, True, execute_inst.ciclosNecessarios))
                execute_situation = EnumReservationStationStates.SUCCESS
        
        elif execute_inst.instrucao == MipsInstructions.LW or execute_inst.instrucao == MipsInstructions.SW:
            if len(self.load_store) < self.getLoadStoreReservationSize():
                self.load_store.append(ReservationStationCell(execute_inst, True, execute_inst.ciclosNecessarios))
                execute_situation = EnumReservationStationStates.SUCCESS
        
        else:
            print('Instrução ainda não suportada!')
            
        if execute_situation == EnumReservationStationStates.SUCCESS:
            self.instruction_queue.remove(execute_inst)
            
        return execute_situation
    
    # Executando cada uma das Reservations Stations e liberando os espaços
    def executeReservations(self):
        inst: ReservationStationCell
        
        tmp = []
        tmp.extend(self.add_sub)
        tmp.extend(self.mul_divide)
        tmp.extend(self.load_store)
        for inst in tmp:
            inst.runCicle()
            
            if inst.isInstrDone():
                try:
                    self.add_sub.remove(inst)
                except:
                    pass # A instrução não é desse banco
            
                try:
                    self.mul_divide.remove(inst)
                except:
                    pass # A instrução não é desse banco
                
                try:
                    self.load_store.remove(inst)
                except:
                    pass
                
                inst.freeCell()

# Celula que armazena o objeto que é inserido nas Reservation Stations
class ReservationStationCell:
    _instrucao: Instrucao
    _isBusy: bool
    _numCiclos: int
    
    def __init__(self) -> None:
        self._instrucao = None
        self._isBusy = False
        self._numCiclos = 0
    
    def __init__(self, inst: Instrucao, isBusy: bool, nCiclos: int) -> None:
        self._instrucao = inst
        self._isBusy = isBusy
        self._numCiclos = nCiclos
        
    def isBusy(self) -> bool:
        return self._isBusy
    
    def freeCell(self) -> None:
        self._isBusy = False
    
    def runCicle(self) -> None:
        self._numCiclos -= 1
        
    def isInstrDone(self) -> bool:
        return self._numCiclos <= 0
    
    def __str__(self) -> str:
        return f'{self._instrucao.getInstr()} | Reserva ocupada: {self._isBusy}'
    
    def __repr__(self) -> str:
        return f'({self.__str__()})'