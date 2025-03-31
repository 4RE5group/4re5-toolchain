# 4re5 asm compiler

| ci| - | - | * | - | u |op1|op0|zx |sw | a | d |*a|lt |eq |gt |
|-- |-- |-- |-- |-- |-- |-- |-- |-- |-- |-- |-- |-- |-- |-- |-- |
|-- |-- |-- |-- |-- |-- |-- |-- |-- |-- |-- |-- |-- |-- |-- |-- |
16 bits

| Instruction | ci  | 2-bit Opcode | u  | lt  | eq  | gt  | zx  | sw  | Description  |
|--|--|--|--|--|--|--|--|--|--|
| MOV | 0 | 00 | 0  | 0 | 0 | 0 | 0 | 0 | Move operation (data transfer) |
| JMP | 0 | 01 | 0  | 0 | 0 | 0 | 0 | 0 | Jump operation  |
| JNE | 0 | 10 | 0  | 0 | 1 | 0 | 0 | 0 | Jump if Not Equal |
| JLT | 0 | 11 | 0  | 1 | 0 | 0 | 0 | 0 | Jump if Less Than Zero  |
| ADD | 1 | 00 | 0  | 0 | 0 | 0 | 0 | 0 | Add operation |
| SUB | 1 | 01 | 0  | 0 | 0 | 0 | 0 | 0 | Subtract operation  |
| INC | 1 | 10 | 0  | 0 | 0 | 0 | 0 | 0 | Increment operation |
| DEC | 1 | 11 | 0  | 0 | 0 | 0 | 0 | 0 | Decrement operation |
| AND | 1 | 00 | 1  | 0 | 0 | 0 | 0 | 0 | Logical AND |
| OR  | 1 | 01 | 1  | 0 | 0 | 0 | 0 | 0 | Logical OR  |
| XOR | 1 | 10 | 1  | 0 | 0 | 0 | 0 | 0 | Logical XOR |
| NOT | 1 | 11 | 1  | 0 | 0 | 0 | 0 | 0 | Logical NOT |
| CMP | 1 | 00 | 0  | 0 | 1 | 0 | 0 | 0 | Compare operation |
| TEST| 1 | 01 | 1  | 0 | 0 | 0 | 1 | 0 | Test operation (set flags)  |
| JGT | 0 | 00 | 0  | 0 | 0 | 1 | 0 | 0 | Jump if Greater Than Zero |
| JEQ | 0 | 01 | 0  | 0 | 1 | 0 | 0 | 0 | Jump if Equal to Zero |
| JZ  | 0 | 10 | 0  | 0 | 1 | 0 | 1 | 0 | Jump if Zero|



u: number operation, u=1 else logic operation


zx: These could be flags or modifier bits used in the operation

sw: Possibly a switch that helps select between different modes or variants of the operation

*a dest reg

d value

a input reg

lt less than
eq equal to
gt greater than