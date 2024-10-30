import sys
from parser import Parser
import code

symbol_table = {
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "SCREEN": 16384,
    "KBD": 24576,
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
}


def pre_pass(lines):
    parser = Parser(lines)
    output = []
    i = 0
    while parser.hasMoreLines():
        i += 1
        parser.advance()
        out = ""
        instructionType = parser.instructionType()
        if instructionType == "L_INSTRUCTION":
            i -= 1
            symbol_table[parser.symbol()] = i
        else:
            out = parser.getLine()
            output.append(out)

    print(output)
    print(symbol_table)

    return output


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def read_and_write(filepath):
    st_size = 16
    with open(filepath, "r") as infile, open(
        filepath.replace("asm", "hack"), "w"
    ) as outfile:
        lines = infile.readlines()
        parser = Parser(pre_pass(lines))
        output = []
        while parser.hasMoreLines():
            parser.advance()
            out = ""
            instructionType = parser.instructionType()
            match instructionType:
                case "A_INSTRUCTION":
                    symbol = parser.symbol()
                    if not is_number(symbol):
                        print(symbol)
                        if symbol in symbol_table:
                            symbol = symbol_table[symbol]
                        else:
                            symbol_table[symbol] = st_size
                            symbol = st_size
                            st_size += 1
                    out = "0" + str(format(int(symbol), "015b"))
                case "C_INSTRUCTION":
                    print(parser.dest(), parser.comp(), parser.jump())
                    out = (
                        "111"
                        + code.comp(parser.comp())
                        + code.dest(parser.dest())
                        + code.jump(parser.jump())
                    )

            print(out)
            output.append(out + "\n")

        outfile.writelines(output)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <filepath>")
    else:
        read_and_write(sys.argv[1])
