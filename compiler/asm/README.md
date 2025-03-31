# 4re5 asm compiler

| ci| - | - | * | - | u |op1|op0|zx |sw | a | d |*a|lt |eq |gt |
|-- |-- |-- |-- |-- |-- |-- |-- |-- |-- |-- |-- |-- |-- |-- |-- |

16 bits
| ci | op num | instruction |
| -- | -- | -- |
| 0 | 00 | MOV |
| 0 | 01 | JMP |
| 0 | 10 | JNE |
| 0 | 10 | JLT |
| 1 | 00 | ADD |
| 1 | 01 | SUB |
| 1 | 10 | INC |
| 1 | 10 | DEC |


u: Might represent a specific mode or flag for the operation


zx: These could be flags or modifier bits used in the operation

sw: Possibly a switch that helps select between different modes or variants of the operation

*a, d, a, lt, eq, gt: These columns may represent conditions or operands used in the instructions, like flags or specific register/address references