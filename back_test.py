import time
import backend.back
import os

b = backend.back.Tomasulo(os.getcwd()+'/assets/instrucoes1.txt')

for i in range(100):
    tmp = b.clock()
    
    if tmp == backend.back.TomasuloStates.FINALIZED:
        break