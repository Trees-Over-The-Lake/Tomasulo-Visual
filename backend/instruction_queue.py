from instruction import Instrucao

class InstructionQueue:
    def __init__(self):
        self.instruction_queue = []
        self.queue_size = 3


    def add_to_instruction_queue(self, i: Instrucao):
        if len(self.instruction_queue) < self.queue_size:
            self.instruction_queue.append(i)
        else:
            print("FILA CHEIA!")


    def stall():
        pass


    def check_true_dependency(self):
        for i in range(0, len(self.instruction_queue)-1):
            for j in range(i+1, len(self.instruction_queue)):
                if (self.instruction_queue[i].instrucao in ['add', 'sub', 'mul', 'div']):
                    
                    if self.instruction_queue[j].rsrc1  == self.instruction_queue[i].rdest or self.instruction_queue[j].rsrc2 == self.instruction_queue[i].rdest:
                        self.instruction_queue[j].add_dependency(self.instruction_queue[i].rdest)

                #elif self.instruction_queue[i].instrucao == 'beq':
                #    if self.instruction_queue[i].rsrc1 == self.instruction_queue[j].rdest or self.instruction_queue[i].rsrc2 == self.instruction_queue[j].rdest:
                #        print(f"Dependencia no beq com {self.instruction_queue[j]}")