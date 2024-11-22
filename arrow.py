import helper
from memory import memory
import sys


_memory = memory()
argv = helper.get_argv()
codes = helper.load_file(argv[1])
codes = codes.split("\n")

for code in codes:
    code = code.split(" ")

    # set value in memory
    if code[0] in helper.init_word:
        if not code[2] == "=":
            print("Error : '=' not ")
            sys.exit()
        _memory.set(code[1], [code[3], code[0]])

    # print function
    if code[0] == "print":
        if code[1][0] == "$":
            print(_memory.get(code[1])[0])

        else:
            for string in code:
                if not string == "print":
                    print(string, end=" ")
            print("")
    
    # casting functions
    if code[0] == "to_str":
        temp = _memory.get(code[1])
        _memory.set(code[1],[temp[0],"str"])