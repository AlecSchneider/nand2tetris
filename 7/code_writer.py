i = 0

statics = {}


def write_arithmetic(command):
    global i
    out = ["// " + command]
    if command == "add":
        out.extend(pop_to_m())
        out.append("D=M")
        out.extend(pop_to_m())
        out.append("D=D+M")
        out.extend(push_d())
    elif command == "eq":
        out.extend(pop_to_m())
        out.append("D=M")
        out.extend(pop_to_m())
        out.append("D=D-M")
        out.extend(true_false(i, "JEQ"))
        out.extend(push_d())

        i += 1
    elif command == "lt":
        out.extend(pop_to_m())
        out.append("D=M")
        out.extend(pop_to_m())
        out.append("D=M-D")
        out.extend(true_false(i, "JLT"))
        out.extend(push_d())

        i += 1
    elif command == "gt":
        out.extend(pop_to_m())
        out.append("D=M")
        out.extend(pop_to_m())
        out.append("D=M-D")
        out.extend(true_false(i, "JGT"))
        out.extend(push_d())

        i += 1
    elif command == "sub":
        out.extend(pop_to_m())
        out.append("D=M")
        out.extend(pop_to_m())
        out.append("D=M-D")
        out.extend(push_d())
    elif command == "neg":
        out.extend(pop_to_m())
        out.append("D=-M")
        out.extend(push_d())
    elif command == "and":
        out.extend(pop_to_m())
        out.append("D=M")
        out.extend(pop_to_m())
        out.append("D=D&M")
        out.extend(push_d())
    elif command == "or":
        out.extend(pop_to_m())
        out.append("D=M")
        out.extend(pop_to_m())
        out.append("D=D|M")
        out.extend(push_d())
    elif command == "not":
        out.extend(pop_to_m())
        out.append("D=!M")
        out.extend(push_d())
    else:
        raise Exception("not implemented")

    return "\n".join(out)


# command = C_PUSH or C_POP
def write_push_pop(command, segment, index):
    out = ["// " + command]
    if command == "C_PUSH":
        out.extend(write_push(segment, index))
        out.extend(push_d())
    elif command == "C_POP":
        out.extend(pop_to_m())
        out.append("D=M")
        out.extend(write_pop(segment, index))
    else:
        raise Exception("not implemented")

    return "\n".join(out)


def write_push(segment, index):
    out = []
    if segment == "constant":
        out.append(f"@{index}")
        out.append("D=A")

    elif segment == "static":
        if index not in statics:
            statics[index] = len(statics) + 16
        out.append(f"@{statics[index]}")
        out.append("D=M")

    elif segment == "temp":
        s = str(int(index) + 5)
        out.append(f"@{s}")
        out.append("D=M")

    else:
        s = ""
        if segment == "local":
            s = "LCL"
        elif segment == "argument":
            s = "ARG"
        elif segment == "this" or (segment == "pointer" and index == "0"):
            s = "THIS"
        elif segment == "that" or (segment == "pointer" and index == "1"):
            s = "THAT"
        else:
            raise Exception("not implemented")

        out.append(f"@{s}")
        if segment != "pointer":
            out.append("A=M")
            for _ in range(int(index)):
                out.append("A=A+1")
        out.append("D=M")

    return out


def write_pop(segment, index):
    out = []
    s = ""
    if segment == "temp":
        s = str(int(index) + 5)
        out.append(f"@{s}")
        out.append("M=D")

    elif segment == "static":
        if index not in statics:
            statics[index] = len(statics) + 16
        out.append(f"@{statics[index]}")
        out.append("M=D")

    else:
        if segment == "local":
            s = "LCL"
        elif segment == "argument":
            s = "ARG"
        elif segment == "this" or (segment == "pointer" and index == "0"):
            s = "THIS"
        elif segment == "that" or (segment == "pointer" and index == "1"):
            s = "THAT"
        else:
            raise Exception("not implemented")

        out.append(f"@{s}")
        if segment != "pointer":
            out.append("A=M")
            for _ in range(int(index)):
                out.append("A=A+1")
        out.append("M=D")

    return out


def push_d():
    out = []
    out.append("@SP")
    out.append("A=M")
    out.append("M=D")
    out.extend(inc_sp())
    return out


def pop_to_m():
    out = []
    out.extend(dec_sp())
    out.append("@SP")
    out.append("A=M")
    return out


def inc_sp():
    out = []
    out.append("@SP")
    out.append("M=M+1")
    return out


def dec_sp():
    out = []
    out.append("@SP")
    out.append("M=M-1")
    return out


def true_false(i, comp):
    out = []
    out.append(f"@TRUE-{str(i)}")
    out.append(f"D;{comp}")
    out.append(f"@FALSE-{str(i)}")
    out.append("0;JMP")
    out.append(f"(TRUE-{i})")
    out.append("D=-1")
    out.append(f"@DONE-{i}")
    out.append("0;JMP")
    out.append(f"(FALSE-{i})")
    out.append("D=0")
    out.append(f"(DONE-{i})")
    return out
