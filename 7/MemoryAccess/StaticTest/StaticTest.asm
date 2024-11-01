// C_PUSH
@111
D=A
@SP
A=M
M=D
@SP
M=M+1
// C_PUSH
@333
D=A
@SP
A=M
M=D
@SP
M=M+1
// C_PUSH
@888
D=A
@SP
A=M
M=D
@SP
M=M+1
// C_POP
@SP
M=M-1
@SP
A=M
D=M
@16
M=D
// C_POP
@SP
M=M-1
@SP
A=M
D=M
@17
M=D
// C_POP
@SP
M=M-1
@SP
A=M
D=M
@18
M=D
// C_PUSH
@17
D=M
@SP
A=M
M=D
@SP
M=M+1
// C_PUSH
@18
D=M
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=M-D
@SP
A=M
M=D
@SP
M=M+1
// C_PUSH
@16
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=D+M
@SP
A=M
M=D
@SP
M=M+1
(END)
@END
0;JMP