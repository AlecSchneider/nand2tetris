// C_PUSH
@3030
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
@THIS
M=D
// C_PUSH
@3040
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
@THAT
M=D
// C_PUSH
@32
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
@THIS
A=M
A=A+1
A=A+1
M=D
// C_PUSH
@46
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
@THAT
A=M
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D
// C_PUSH
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// C_PUSH
@THAT
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
// C_PUSH
@THIS
A=M
A=A+1
A=A+1
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
@THAT
A=M
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
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