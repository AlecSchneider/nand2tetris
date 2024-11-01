import sys
from parser import Parser
import code_writer


def read_and_write(filepath):
    st_size = 16
    with open(filepath, "r") as infile, open(
        filepath.replace("vm", "asm"), "w"
    ) as outfile:
        lines = infile.readlines()
        parser = Parser(lines)
        output = []
        while parser.has_more_lines():
            parser.advance()
            out = ""
            command_type = parser.command_type()

            if command_type in ["C_PUSH", "C_POP"]:
                out = code_writer.write_push_pop(
                    command_type, parser.arg1(), parser.arg2()
                )
            elif command_type == "C_ARITHMETIC":
                out = code_writer.write_arithmetic(parser.arg1())
            else:
                raise Exception("not implemented")
            print(out)
            output.append(out + "\n")

        output.append("(END)\n@END\n0;JMP")
        outfile.writelines(output)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <filepath>")
    else:
        read_and_write(sys.argv[1])
