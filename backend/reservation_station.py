# Backend do tomasulo, lendo e despachando as intruções

from backend.MIPS.instructions import MipsInstructions
from backend.instruction import Instrucao
import enum

class EnumReservationStationStates(enum.Enum):
    SUCCESS = 1
    BUSY = 2

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
    
    def isInstructionQueueBusy(self):
        print(len(self.instruction_queue))
        return len(self.instruction_queue) == self.getInstructionQeueReservationSize()
    
    # Insert a new instruction in the reservation station
    def insertInstruction(self, i: Instrucao):
        # Inserindo na fila de instruções
        
        if i.instrucao == MipsInstructions.ADD or i.instrucao == MipsInstructions.SUB:
            # Considerando que não há RAW ou WAR
            if len(self.add_sub) < self.getAddSubReservationSize():
                self.add_sub.append(ReservationStationCell(i, True))
                return EnumReservationStationStates.SUCCESS
                              
            else:
                return EnumReservationStationStates.BUSY # Reserva cheia
        
        elif i.instrucao == MipsInstructions.MUL or i.instrucao == MipsInstructions.DIV:
            if len(self.mul_divide) < self.getMulDivideReservationSize():
                self.mul_divide.append(ReservationStationCell(i, True))
                return EnumReservationStationStates.SUCCESS
                              
            else:
                return EnumReservationStationStates.BUSY # Reserva cheia
        
        elif i.instrucao == MipsInstructions.LW or i.instrucao == MipsInstructions.SW:
            if len(self.load_store) < self.getLoadStoreReservationSize():
                self.load_store.append(ReservationStationCell(i, True))
                return EnumReservationStationStates.SUCCESS
                              
            else:
                return EnumReservationStationStates.BUSY # Reserva cheia
        
        else:
            print('Instrução ainda não suportada!')

# Celula que armazena o objeto que é inserido nas Reservation Stations
class ReservationStationCell:
    _instrucao: Instrucao
    _isBusy: bool
    
    def __init__(self) -> None:
        self._instrucao = None
        self._isBusy = False
    
    def __init__(self, inst: Instrucao, isBusy: bool) -> None:
        self._instrucao = inst
        self._isBusy = isBusy
        
    def isBusy(self):
        return self._isBusy
    
    def __str__(self) -> str:
        return f'{self._instrucao.getInstr()} | Reserva ocupada: {self._isBusy}'