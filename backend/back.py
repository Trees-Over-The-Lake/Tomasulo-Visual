import enum
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
        if len(self.instrucoes) == 0:
            return TomasuloStates.FINALIZED
        
        # Verificando se há espaço para uma nova instrução
        if self.reservationStation.isInstructionQueueBusy():
            return TomasuloStates.BUSY
        
        
        # Pegando uma nova instrução para inserir na fila de instruções
        next_instr = self.instrucoes.pop(0)
        self.reservationStation.insertInstruction(next_instr)
        
        # Despachando uma instrução para uma Reservation Station
        #if len(self.reservationStation.getInstructionQeueReservationSize()) > 0:
        return TomasuloStates.SUCCESS