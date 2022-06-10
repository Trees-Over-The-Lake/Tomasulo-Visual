from back import Back
import os

b = Back(os.getcwd()+'/../assets/instrucoes.txt')

print(b.getInstrucoesAndCiclos())