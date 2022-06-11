import backend.back
import os

b = backend.back.Tomasulo(os.getcwd()+'/assets/instrucoes.txt')

for i in range(100):
    tmp = b.clock()
    
    if not backend.back.TomasuloStates.FINALIZED:
        print(tmp)