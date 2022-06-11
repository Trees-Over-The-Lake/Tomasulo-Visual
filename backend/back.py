import enum
import random
from backend.MIPS.instructions import MipsInstructions
from backend.instruction import Instrucao
from backend.parse_instructions import ParseInstructions
from backend.reservation_station import ReservationStation

class TomasuloStates(enum.Enum):
    SUCCESS = 1
    BUSY = 2
    FINALIZED = 3

# Classe para controlar todo o algoritmo de Tomasulo
class Tomasulo:
    # Fazendo todas as operações básicas antes de iniciar o tomasulo
    def __init__(self, path) -> None:
        parseInstructions = ParseInstructions(path)
        self.instrucoes = parseInstructions.getInstrucoes()
        self.instrucoesECiclos = parseInstructions.getInstrucoesAndCiclos()
        
        # Criando uma Reservation Station
        self.reservationStation = ReservationStation()
        
    # Executando um clock da CPU para executar o algoritmo
    def clock(self):
        print(self.reservationStation.add_sub, self.reservationStation.mul_divide, self.reservationStation.load_store)
        
        if len(self.instrucoes) == 0 and self.reservationStation.isAllReservationsStationsEmpty():
            return TomasuloStates.FINALIZED
        
        # Verificando se há espaço para uma nova instrução
        if self.reservationStation.isInstructionQueueFull():
            return TomasuloStates.BUSY
        
        else:
            # Pegando uma nova instrução para inserir na fila de instruções
            if len(self.instrucoes) > 0:
                next_instr: Instrucao = self.instrucoes.pop(0)
                
                # Descartando de 0 a 3 instruções aleatoriamente
                if next_instr.instrucao == MipsInstructions.BEQ:
                    for _ in range(random.randint(0, min(len(self.instrucoes), 3))):
                        self.instrucoes.pop(0)
                
                else:
                    self.reservationStation.insertInstruction(next_instr)            
        

        # Executando as Reservations Stations
        self.reservationStation.executeReservations()
        
        # Ao chegar aqui tudo rodou como esperado
        return TomasuloStates.SUCCESS