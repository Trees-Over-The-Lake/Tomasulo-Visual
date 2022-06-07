# Arquivo contendo todas as instruções suportadas pelo MIPS

class MipsInstructions:    
    # Instruções aritméticas
    ADD   = 'add'  # add a, b, c 	a = b + c 	adds signed numbers.
    ADDU  = 'addu' # adds unsigned numbers.
    SUB   = 'sub'  # subtracts signed numbers.
    SUB_U = 'subu' # Unsigned subtraction
    MUL   = 'mul'  # gives low 32 bits of signed multiplication.
    MUL_U = 'mulu' # Unsigned multiplication
    DIV   = 'div'  # gives quotient of signed division.
    DIV_U = 'divu' # Unsigned division
    REM   = 'rem'  # gives remainder of signed division.
    REM_U = 'remu' # Unsigned Remainder of division
    MHFI  = 'mfhi' # after mul, gives high 32 bits. after div, gives remainder.
    MFLO  = 'mflo' # after mul, gives low 32 bits. after div, gives quotient.

    # Instruções lógicas
    NEG = 'neg' # neg a, b 	    a = -b 	gives the negative of b.
    AND = 'and' # a = b & c 	bitwise ANDs numbers.
    OR  = 'or'  # a = b | c 	bitwise ORs numbers.
    XOR = 'xor' # a = b ^ c 	bitwise XORs numbers.
    
    # Instruções de desvio
    
    # Instruções de descarte