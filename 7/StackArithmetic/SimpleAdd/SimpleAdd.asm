// C_PUSH
@7
D=A
@SP
A=M
M=D
@SP
M=M+1
// C_PUSH
@8
D=A
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