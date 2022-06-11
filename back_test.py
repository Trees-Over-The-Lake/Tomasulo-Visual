import time
import backend.back
import os

b = backend.back.Tomasulo(os.getcwd()+'/assets/instrucoes.txt')

for i in range(100):
    tmp = b.clock()
    print(tmp)
    
    if tmp == backend.back.TomasuloStates.FINALIZED:
        print("Fila de instruções limpa!")
        break