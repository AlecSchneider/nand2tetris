def dest(instruction):
    match instruction:
        case "M":
            return "001"
        case "D":
            return "010"
        case "DM":
            return "011"
        case "MD":
            return "011"
        case "A":
            return "100"
        case "AM":
            return "101"
        case "MA":
            return "101"
        case "AD":
            return "110"
        case "DA":
            return "110"
        case "ADM":
            return "111"
        case "AMD":
            return "111"
        case "DAM":
            return "111"
        case "DMA":
            return "111"
        case "MDA":
            return "111"
        case "MAD":
            return "111"
    return "000"


def comp(instruction):
    a_zero = "0"
    a_one = "1"
    match instruction:
        # a = 0
        case "0":
            return a_zero + "101010"
        case "1":
            return a_zero + "111111"
        case "-1":
            return a_zero + "111010"
        case "D":
            return a_zero + "001100"
        case "A":
            return a_zero + "110000"
        case "!D":
            return a_zero + "001101"
        case "!A":
            return a_zero + "110001"
        case "-D":
            return a_zero + "001111"
        case "-A":
            return a_zero + "110011"
        case "D+1":
            return a_zero + "011111"
        case "A+1":
            return a_zero + "110111"
        case "D-1":
            return a_zero + "001110"
        case "A-1":
            return a_zero + "110010"
        case "D+A":
            return a_zero + "000010"
        case "D-A":
            return a_zero + "010011"
        case "A-D":
            return a_zero + "000111"
        case "D&A":
            return a_zero + "000000"
        case "D|A":
            return a_zero + "010101"

        # a = 1
        case "M":
            return a_one + "110000"
        case "!M":
            return a_one + "110001"
        case "-M":
            return a_one + "110011"
        case "M+1":
            return a_one + "110111"
        case "M-1":
            return a_one + "110010"
        case "D+M":
            return a_one + "000010"
        case "D-M":
            return a_one + "010011"
        case "M-D":
            return a_one + "000111"
        case "D&M":
            return a_one + "000000"
        case "D|M":
            return a_one + "010101"


def jump(instruction):
    match instruction:
        case "JGT":
            return "001"
        case "JEQ":
            return "010"
        case "JGE":
            return "011"
        case "JLT":
            return "100"
        case "JNE":
            return "101"
        case "JLE":
            return "110"
        case "JMP":
            return "111"
    return "000"
