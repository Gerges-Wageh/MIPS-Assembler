def Assembler():
    # Register_Converter_Function
    def Regs_Converter(Reg):
        if "$ZERO" in Reg:
            Reg = "00000"
        elif "$at" in Reg:
            Reg = "00001"
        elif "$v0" in Reg:
            Reg = "00010"
        elif "$v1" in Reg:
            Reg = "00011"
        elif "$a0" in Reg:
            Reg = "00100"
        elif "$a1" in Reg:
            Reg = "00101"
        elif "$a2" in Reg:
            Reg = "00110"
        elif "$a3" in Reg:
            Reg = "00111"
        elif "$t0" in Reg:
            Reg = "01000"
        elif "$t1" in Reg:
            Reg = "01001"
        elif "$t2" in Reg:
            Reg = "01010"
        elif "$t3" in Reg:
            Reg = "01011"
        elif "$t4" in Reg:
            Reg = "01100"
        elif "$t5" in Reg:
            Reg = "01101"
        elif "$t6" in Reg:
            Reg = "01110"
        elif "$t7" in Reg:
            Reg = "01111"
        elif "$s0" in Reg:
            Reg = "10000"
        elif "$s1" in Reg:
            Reg = "10001"
        elif "$s2" in Reg:
            Reg = "10010"
        elif "$s3" in Reg:
            Reg = "10011"
        elif "$s4" in Reg:
            Reg = "10100"
        elif "$s5" in Reg:
            Reg = "10101"
        elif "$s6" in Reg:
            Reg = "10110"
        elif "$s7" in Reg:
            Reg = "10111"
        elif "$t8" in Reg:
            Reg = "11000"
        elif "$t9" in Reg:
            Reg = "11001"
        elif "$k0" in Reg:
            Reg = "11010"
        elif "$k1" in Reg:
            Reg = "11011"
        elif "$gp" in Reg:
            Reg = "11100"
        elif "$sp" in Reg:
            Reg = "11101"
        elif "$fp" in Reg:
            Reg = "11110"
        elif "$ra" in Reg:
            Reg = "11111"
        return Reg

    # OP_Code Function

    def OP_Code(OP):
        if OP == "add":
            OP = "000000"
        elif OP == "addi":
            OP = "001000"
        elif OP == "and":
            OP = "000000"
        elif OP == "andi":
            OP = "001100"
        elif OP == "beq":
            OP = "000100"
        elif OP == "bne":
            OP = "000101"
        elif OP == "j":
            OP = "000010"
        elif OP == "jal":
            OP = "000011"
        elif OP == "jr":
            OP = "000000"
        elif OP == "lw":
            OP = "100011"
        elif OP == "nor":
            OP = "000000"
        elif OP == "or":
            OP = "000000"
        elif OP == "ori":
            OP = "001101"
        elif OP == "sll":
            OP = "000000"
        elif OP == "slt":
            OP = "000000"
        elif OP == "sub":
            OP = "000000"
        elif OP == "sw":
            OP = "101011"
        return OP

    # Shamt_Function

    def Shamt_Funtion(Shamt):
        out = bin(int(Shamt)).replace("b", "0")
        while len(out) < 5:
            out = "0" + out
        return out

    # J-Address_Function
    def J_Address(label):
        out = bin(label).replace("b", "0")
        while len(out) < 26:
            out = "0" + out
        return out

    # branch_address_fuction
    def Branch_Address(num):
        if num >= 0:
            out = bin(num).replace("b", "0")
            while len(out) < 16:
                out = "0" + out
        elif num < 0:
            num = num * -1
            out = bin(num).replace("b", "0")
            while len(out) < 16:
                out = "0" + out
            out = out[::-1]
            flag = out.index("1")
            musk = out[0:flag + 1]
            for m in range(flag + 1, 16):
                if out[m] == "0":
                    musk = musk + "1"
                elif out[m] == "1":
                    musk = musk + "0"
            out = musk[::-1]

        return out

    # Func_Function
    def Func(s):
        if s == "add":
            s = "100000"
        elif s == "and":
            s = "100100"
        elif s == "jr":
            s = "001000"
        elif s == "nor":
            s = "100111"
        elif s == "or":
            s = "100101"
        elif s == "sll":
            s = "000000"
        elif s == "slt":
            s = "101010"
        elif s == "sub":
            s = "100010"
        return s

    Assembly = open("Assembly.txt", "r")
    parts = Assembly.readlines()
    for i in range(len(parts)):
        insts = parts[i].split()
        if len(insts) == 4:
            if (insts[0] == "add" or
                    insts[0] == "and" or
                    insts[0] == "nor" or
                    insts[0] == "or" or
                    insts[0] == "slt" or
                    insts[0] == "sub"):
                MC = (OP_Code(insts[0]) + Regs_Converter(insts[2]) + Regs_Converter(insts[3]) +
                      Regs_Converter(insts[1]) + "00000" + Func(insts[0]))
                Machine_Code = open("Machine_Code.txt", "a")
                if i == 0:
                    Machine_Code.write(MC)
                else:
                    Machine_Code.write("\n" + MC)
            elif insts[0] == "sll":
                MC = (OP_Code(insts[0]) + "00000" + Regs_Converter(insts[2]) + Regs_Converter(insts[1]) +
                      Shamt_Funtion(insts[3]) + Func(insts[0]))
                Machine_Code = open("Machine_Code.txt", "a")
                if i == 0:
                    Machine_Code.write(MC)
                else:
                    Machine_Code.write("\n" + MC)
            elif insts[0] == "beq":
                beq_index = 0
                for Bi in range(len(parts)):
                    if parts[Bi].startswith(insts[3]):
                        beq_index = Bi
                MC = (OP_Code(insts[0]) + Regs_Converter(insts[1]) + Regs_Converter(insts[2]) + Branch_Address(
                    (beq_index - i) - 1))
                Machine_Code = open("Machine_Code.txt", "a")
                if i == 0:
                    Machine_Code.write(MC)
                else:
                    Machine_Code.write("\n" + MC)
            elif insts[0] == "bne":
                beq_index = 0
                for Bi in range(len(parts)):
                    if parts[Bi].startswith(insts[3]):
                        beq_index = Bi
                MC = (OP_Code(insts[0]) + Regs_Converter(insts[1]) + Regs_Converter(insts[2]) + Branch_Address(
                    (beq_index - i) - 1))
                Machine_Code = open("Machine_Code.txt", "a")
                if i == 0:
                    Machine_Code.write(MC)
                else:
                    Machine_Code.write("\n" + MC)
            elif insts[0] == "ori" or insts[0] == "addi":
                MC = OP_Code(insts[0]) + Regs_Converter(insts[1]) + Regs_Converter(insts[2]) + Branch_Address(
                    int(insts[3]))
                Machine_Code = open("Machine_Code.txt", "a")
                if i == 0:
                    Machine_Code.write(MC)
                else:
                    Machine_Code.write("\n" + MC)
            elif insts[0] == "lw" or insts[0] == "sw":
                MC = OP_Code(insts[0]) + Regs_Converter(insts[3]) + Regs_Converter(insts[1]) + Branch_Address(
                    int(insts[2]))
                Machine_Code = open("Machine_Code.txt", "a")
                if i == 0:
                    Machine_Code.write(MC)
                else:
                    Machine_Code.write("\n" + MC)


        elif len(insts) == 5:
            if (insts[1] == "add" or
                    insts[1] == "and" or
                    insts[1] == "nor" or
                    insts[1] == "or" or
                    insts[1] == "slt" or
                    insts[1] == "sub"):
                MC = (OP_Code(insts[1]) + Regs_Converter(insts[3]) + Regs_Converter(insts[4]) +
                      Regs_Converter(insts[2]) + "00000" + Func(insts[1]))
                Machine_Code = open("Machine_Code.txt", "a")
                if i == 0:
                    Machine_Code.write(MC)
                else:
                    Machine_Code.write("\n" + MC)
            elif insts[1] == "sll":
                MC = (OP_Code(insts[1]) + "00000" + Regs_Converter(insts[3]) + Regs_Converter(insts[2]) +
                      Shamt_Funtion(insts[4]) + Func(insts[1]))
                Machine_Code = open("Machine_Code.txt", "a")
                if i == 0:
                    Machine_Code.write(MC)
                else:
                    Machine_Code.write("\n" + MC)
            elif insts[1] == "beq":
                beq_index = 0
                for Bi in range(len(parts)):
                    if parts[Bi].startswith(insts[4]):
                        beq_index = Bi
                MC = (OP_Code(insts[1]) + Regs_Converter(insts[2]) + Regs_Converter(insts[3]) + Branch_Address(
                    (beq_index - i) - 1))
                Machine_Code = open("Machine_Code.txt", "a")
                if i == 0:
                    Machine_Code.write(MC)
                else:
                    Machine_Code.write("\n" + MC)
            elif insts[1] == "bne":
                beq_index = 0
                for Bi in range(len(parts)):
                    if parts[Bi].startswith(insts[4]):
                        beq_index = Bi
                MC = (OP_Code(insts[1]) + Regs_Converter(insts[2]) + Regs_Converter(insts[3]) + Branch_Address(
                    (beq_index - i) - 1))
                Machine_Code = open("Machine_Code.txt", "a")
                if i == 0:
                    Machine_Code.write(MC)
                else:
                    Machine_Code.write("\n" + MC)
            elif insts[1] == "ori" or insts[0] == "addi":
                MC = (OP_Code(insts[1]) + Regs_Converter(insts[2]) + Regs_Converter(insts[3]) + Branch_Address(
                    int(insts[4])))
                Machine_Code = open("Machine_Code.txt", "a")
                if i == 0:
                    Machine_Code.write(MC)
                else:
                    Machine_Code.write("\n" + MC)
            elif insts[1] == "lw" or insts[1] == "sw":
                MC = (OP_Code(insts[1]) + Regs_Converter(insts[4]) + Regs_Converter(insts[2]) + Branch_Address(
                    int(insts[3])))
                Machine_Code = open("Machine_Code.txt", "a")
                if i == 0:
                    Machine_Code.write(MC)
                else:
                    Machine_Code.write("\n" + MC)
        elif len(insts) == 2:
            if insts[0] == "jr":
                MC = "00000011111000000000000000001000"
                Machine_Code = open("Machine_Code.txt", "a")
                if i == 0:
                    Machine_Code.write(MC)
                else:
                    Machine_Code.write("\n" + MC)
            elif insts[0] == "j":
                for j in range(len(parts)):
                    if parts[j].startswith(insts[1]):
                        index = j
                MC = OP_Code(insts[0]) + J_Address(index)
                Machine_Code = open("Machine_Code.txt", "a")
                if i == 0:
                    Machine_Code.write(MC)
                else:
                    Machine_Code.write("\n" + MC)
            elif insts[0] == "jal":
                for j in range(len(parts)):
                    if parts[j].startswith(insts[1]):
                        index = j
                MC = OP_Code(insts[0]) + J_Address(index)
                Machine_Code = open("Machine_Code.txt", "a")
                if i == 0:
                    Machine_Code.write(MC)
                else:
                    Machine_Code.write("\n" + MC)
        elif len(insts) == 3:
            if insts[1] == "jr":
                MC = "00000011111000000000000000001000"
                Machine_Code = open("Machine_Code.txt", "a")
                if i == 0:
                    Machine_Code.write(MC)
                else:
                    Machine_Code.write("\n" + MC)
            elif insts[1] == "j":
                for j in range(len(parts)):
                    if parts[j].startswith(insts[1]):
                        index = j
                MC = OP_Code(insts[1]) + J_Address(index)
                Machine_Code = open("Machine_Code.txt", "a")
                if i == 0:
                    Machine_Code.write(MC)
                else:
                    Machine_Code.write("\n" + MC)
            elif insts[1] == "jal":
                for j in range(len(parts)):
                    if parts[j].startswith(insts[1]):
                        index = j
                MC = OP_Code(insts[1]) + J_Address(index)
                Machine_Code = open("Machine_Code.txt", "a")
                if i == 0:
                    Machine_Code.write(MC)
                else:
                    Machine_Code.write("\n" + MC)


            
Assembler()