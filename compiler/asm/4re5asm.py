import os

instructions = {
    "MOV":  b"",
    "JMP":  b"",
    "JNE":  b"",
    "JLT":  b"",
    "ADD":  b"",
    "SUB":  b"",
    "INC":  b"",
    "DEC":  b"",
    "AND":  b"",
    "OR" :  b"",
    "XOR":  b"",
    "NOT":  b"",
    "CMP":  b"",
    "TEST": b"",
    "JGT":  b"",
    "JEQ":  b"",
    "JZ":   b""
}

with open("test/test.o", 'r') as file:
    lines = file.readlines()
    for line in lines:
        line=line.strip()
        if not line or line.startswith(';'):
            continue
        
        parts = line.split(' ')  # split instruction and operands
        instruction = parts[0].upper()
        operands = parts[1] if len(parts) > 1 else ""
        
        if instructions.get(instruction) is not None:
            print(f"Valid: {instruction} {operands}")
        else:
            print(f"Invalid instruction: {instruction}")