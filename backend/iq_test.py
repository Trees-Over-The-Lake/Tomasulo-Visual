from instruction_queue import InstructionQueue
from instruction import Instrucao

a = InstructionQueue()
a.add_to_instruction_queue(Instrucao(1, "add", "r1", "r2", "r3"))
a.add_to_instruction_queue(Instrucao(1, "mul", "r2", "r1", "r3"))
a.add_to_instruction_queue(Instrucao(1, "sub", "r1", "r1", "r2"))

a.check_true_dependency()