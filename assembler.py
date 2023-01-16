import sys

inp=[]
loop={}
gvariables={}
l_num = 0
var_count = 0
opcode = ["add", "sub", "mov", "ld", "st", "mul", "div",
          "rs", "ls", "xor", "or", "and", "not", "cmp", "jmp",
          "jlt", "jgt", "je", "movf", "addf", "subf" , "hlt" , "FLAGS"]
reg_to_bin={
    "R0":"000",
    "R1":"001",
    "R2":"010",
    "R3":"011",
    "R4":"100",
    "R5":"101",
    "R6":"110",
    "FLAGS":"111"
}
reg_to_bin2 = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]

varnum=0
error=""
binary_ans=""
check=0

def count_no_var():
    global varnum
    for i in inp:
        if (len(i) == 0):
            continue
        elif(i.split()[0] == "var"):
            varnum += 1



def var_counter():
    global var_count
    for i in inp:
        if (len(i) == 0):
            var_count += 1
        elif (i.split()[0] == "var"):
            var_count += 1
        else:
            break

def label_counter():
    c=0
    for i in inp:
        c+=1
        if (len(i) == 0):
            continue
        elif(i.split()[0][-1]==":" ):
            loop[i.split()[0][:-1]]=c-1

def good_variable():
    c=0
    for i in inp: 
        c+=1
        if (len(i) == 0):
            continue
        elif(i.split()[0]=="var" and len(i.split()) == 2):
            gvariables[i.split()[1]]=len(inp)-varnum+c

def decitobin(n):
    n=int(n)
    if n==0:
        return 0
    else:
        l=[]
        while n!=0:
            l.append(str(n%2))
            n//=2
        while len(l)<8:
            l.append("0")
        l.reverse()
        return ''.join(l)

def decitobin2(n):
    n=int(n)
    if n==0:
        return 0
    else:
        l=[]
        while n!=0:
            l.append(str(n%2))
            n//=2
        while len(l)<4:
            l.append("0")
        l.reverse()
        return ''.join(l)

def point(n):
    n = int(n)
    l=[]
    c=0
    for i in range(4):
        n = n/(10**len(str(n)))
        k=n*2
        l.append(str(k).split(".")[0])
        n=str(k).split(".")[1]
        n = int(n)
        if n==0:
            c=1
            break

    if len(l)<4:
        for i in range(4-len(l)):
            l.append("0")
    
    if c==1:
        return ''.join(l)
    else:
        return "Floating point error"

def floatbin(n):
    a , b = str(n).split(".")
    ans=''
    ans += decitobin2(a)

    ans+=point(b)
    return ans


def var_converter(i, ch):
    global error
    global check
    global l_num
    if ch==0 :
        check = 1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==1:
        check = 1
        error += f"error gen in {l_num} line Illegal use of FLAGS register\n"
    elif ch==2:
        check = 1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==3:
        check = 1
        error += f"error gen in {l_num} line Misuse of labels as variables or vice-versa\n"
    elif ch == 5:
        check = 1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==4:
        pass

def xor_converter(i, ch):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check=1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==1:
        check = 1
        error += f"error gen in {l_num} line Illegal use of FLAGS register\n"
    elif ch==3:
        check =1
        error +=f"error gen in {l_num} line Typo in register name\n"
    elif ch==2:
        binary_ans += "1101000"+reg_to_bin[i[1]]+reg_to_bin[i[2]]+reg_to_bin[i[3]]+"\n"

def mov1_converter(i, ch):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check = 1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==1:
        check = 1
        error +=f"error gen in {l_num} line Illegal use of FLAGS register\n"
    elif ch==2:
        binary_ans += "10010"+reg_to_bin[i[1]]+decitobin(i[2][1:])+"\n"
    elif ch==5:
        check = 1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==6:
        check = 1
        error +=f"error gen in {l_num} line Typo in register name\n"
    else:
        check = 1
        error +=f"error gen in {l_num} line General syntax error\n"

def movf_converter(i, ch):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check = 1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==1:
        check = 1
        error +=f"error gen in {l_num} line Illegal use of FLAGS register\n"
    elif ch==2:
        binary_ans += "00010"+reg_to_bin[i[1]]+floatbin(i[2][1:])+"\n"
    elif ch==3:
        check = 1
        error+=f"error gen in {l_num} line Illegal Immediate values\n"
    elif ch==4:
        check = 1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==5:
        check = 1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==6:
        check = 1
        error +=f"error gen in {l_num} line Typo in register name\n"
    else:
        check = 1
        error +=f"error gen in {l_num} line General syntax error\n"

def add_converter(i, ch, k):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check=1
        error +=f"error gen in {l_num} line General syntax error\n"
    elif ch==1:
        check = 1
        
        error +=f"error gen in {l_num} line Illegal use of FLAGS register\n"
    elif ch==3:
        check =1
    
        error +=f"error gen in {l_num} line Typo in register name\n"
    elif ch==2:
        if k==0:
            binary_ans += "1000000"+reg_to_bin[i[1]]+reg_to_bin[i[2]]+reg_to_bin[i[3]]+"\n"
        else:
            binary_ans += "0000000"+reg_to_bin[i[1]]+reg_to_bin[i[2]]+reg_to_bin[i[3]]+"\n"

def mov2_converter(i, ch):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check = 1
        error += f"error gen in {l_num} line General Syntax error\n"
    
    elif ch==2:
        binary_ans += "1001100000"+reg_to_bin[i[1]]+reg_to_bin[i[2]]+"\n"
    elif ch==5:
        binary_ans += "1001100000"+"111"+reg_to_bin[i[2]]+"\n"
    elif ch==6:
        binary_ans += "1001100000"+reg_to_bin[i[1]]+"111"+"\n"
    elif ch==3:
        check = 1
        error +=f"error gen in {l_num} line Typo in register name\n"
    elif ch==4:
        check = 1
        error += f"error gen in {l_num} line General syntax error\n"

def hlt_converter(i, ch):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check=1
        error += f"error gen in {l_num} line Typo in register name\n"
    else:  
        binary_ans += "0101000000000000"+"\n"

def hlt_converter2(i, ch):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check=1
        error += f"error gen in {l_num} line Typo in register name\n"
    else:  
        binary_ans += "0101000000000000"+"\n"
        
def rs_converter(i, ch):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check = 1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==1:
        check = 1
        error += f"error gen in {l_num} line Illegal use of FLAGS register\n"
    elif ch==3:
        check = 1
        error+=f"error gen in {l_num} line Illegal Immediate values\n"
    elif ch==4:
        check = 1
        error +=f"error gen in {l_num} line General syntax error\n"
    elif ch==5:
        check = 1
        error +=f"error gen in {l_num} line General syntax error\n"
    elif ch==6:
        check = 1
        error += f"error gen in {l_num} line Typo in register name\n"
    elif ch==2:
        binary_ans += "11000"+reg_to_bin[i[1]]+decitobin(i[2][1:])+"\n"

def sub_converter(i, ch, k):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check=1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==1:
        check = 1
        error += f"error gen in {l_num} line Illegal use of FLAGS register\n"
    elif ch==3:
        check =1
        error += f"error gen in {l_num} line Typo in register name\n"
    elif ch==2:
        if k==0:
            binary_ans += "1000100"+reg_to_bin[i[1]]+reg_to_bin[i[2]]+reg_to_bin[i[3]]+"\n"
        else:
            binary_ans += "0000100"+reg_to_bin[i[1]]+reg_to_bin[i[2]]+reg_to_bin[i[3]]+"\n"
        
def mul_converter(i, ch):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check=1
        error +=f"error gen in {l_num} line General syntax error\n"
    elif ch==1:
        check = 1
        error += f"error gen in {l_num} line Illegal use of FLAGS register\n"
    elif ch==3:
        check =1
        error += f"error gen in {l_num} line Typo in register name\n"
    elif ch==2:
        binary_ans += "1011000"+reg_to_bin[i[1]]+reg_to_bin[i[2]]+reg_to_bin[i[3]]+"\n"

def div_converter(i, ch):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check=1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==1:
        check = 1
        error += f"error gen in {l_num} line Illegal use of FLAGS register\n"
    elif ch==3:
        check =1
        error += f"error gen in {l_num} line Typo in register name\n"
    elif ch==2:
        binary_ans += "1011100000"+reg_to_bin[i[1]]+reg_to_bin[i[2]]+"\n"

def ls_converter(i, ch):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check = 1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==1:
        check = 1
        error += f"error gen in {l_num} line Illegal use of FLAGS register\n"
    elif ch==3:
        check = 1
        error+=f"error gen in {l_num} line Illegal Immediate values\n"
    elif ch==4:
        check = 1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==5:
        check = 1
        error +=f"error gen in {l_num} line General syntax error\n"
    elif ch==6:
        check = 1
        error += f"error gen in {l_num} line Typo in register name\n"
    elif ch==2:
        binary_ans += "11001"+reg_to_bin[i[1]]+decitobin(i[2][1:])+"\n"

def jmp_converter(i, ch):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check=1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==3:
        check = 1
        error +=f"error gen in {l_num} line Use of undefined labels\n"
    elif ch==1:
        binary_ans += "11111000"+decitobin(str(loop[i[1]] - varnum)) +"\n"
    elif ch==2:
        binary_ans += "11111000"+decitobin(str(gvariables[i[1]] - varnum))+"\n"


def ld_converter(i, ch):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check=1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==1:
        check = 1
        error += f"error gen in {l_num} line Illegal use of FLAGS register\n"
    elif ch==3:
        check =1
        error += f"error gen in {l_num} line Misuse of labels as variables or vice-versa\n"
    elif ch==4:
        check = 1
        error += f"error gen in {l_num} line Use of undefined variables\n"
    elif ch==2:
        binary_ans += "10100"+reg_to_bin[i[1]]+decitobin(str(gvariables[i[2]]))+"\n"

def st_converter(i, ch):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check=1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==1:
        check = 1
        error +=f"error gen in {l_num} line Illegal use of FLAGS register\n"
    elif ch==3:
        check =1
        error += f"error gen in {l_num} line Misuse of labels as variables or vice-versa\n"
    elif ch==4:
        check = 1
        error += f"error gen in {l_num} line Use of undefined variables\n"
    elif ch==2:
        binary_ans += "10101"+reg_to_bin[i[1]]+decitobin(str(gvariables[i[2]]-1))+"\n"

def jlt_converter(i, ch):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check=1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==3:
        check=1
        error += f"error gen in {l_num} line Use of undefined labels\n"
    elif ch == 1:
        binary_ans += "01100000"+decitobin(str(loop[i[1]] - varnum))+"\n"
    elif ch == 2:
        binary_ans += "01100000"+decitobin(str(gvariables[i[1]] - varnum))+"\n"


def orr_converter(i, ch):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check=1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==1:
        check = 1
        error += f"error gen in {l_num} line Illegal use of FLAGS register\n"
    elif ch==3:
        check =1
        error += f"error gen in {l_num} line Typo in register name\n"
    elif ch==2:
        binary_ans += "1101100"+reg_to_bin[i[1]]+reg_to_bin[i[2]]+reg_to_bin[i[3]]+"\n"

def jgt_converter(i, ch):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check=1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==3:
        check = 1
        error += f"error gen in {l_num} line Use of undefined labels\n"
    elif ch==1:
        binary_ans += "01101000"+decitobin(str(loop[i[1]] - varnum))+"\n"
    elif ch==2:
        binary_ans += "01101000"+decitobin(str(gvariables[i[1]] - varnum))+"\n"


def andd_converter(i, ch):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check=1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==1:
        check = 1
        error += f"error gen in {l_num} line Illegal use of FLAGS register\n"
    elif ch==3:
        check =1
        error += f"error gen in {l_num} line Typo in register name\n"
    elif ch==2:
        binary_ans += "1110000"+reg_to_bin[i[1]]+reg_to_bin[i[2]]+reg_to_bin[i[3]]+"\n"
        
def nott_converter(i, ch):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check=1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==1:
        check = 1
        error += f"error gen in {l_num} line Illegal use of FLAGS register\n"
    elif ch==3:
        check =1
        error +=f"error gen in {l_num} line Typo in register name\n"
    elif ch==2:
        binary_ans += "1110100000"+reg_to_bin[i[1]]+reg_to_bin[i[2]]+"\n"
        
def je_converter(i, ch):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check=1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==3:
        check = 1
        error +=f"error gen in {l_num} line Use of undefined labels\n"
    elif ch==1:
        binary_ans += "01111000"+decitobin(str(loop[i[1]] - varnum))+"\n"
    elif ch==2:
        binary_ans += "01111000"+decitobin(str(gvariables[i[1]] - varnum))+"\n"


def cmp_converter(i, ch):
    global error
    global binary_ans
    global check
    global l_num
    if ch==0:
        check=1
        error += f"error gen in {l_num} line General syntax error\n"
    elif ch==1:
        check = 1
        error += f"error gen in {l_num} line Illegal use of FLAGS register\n"
    elif ch==3:
        check =1
        error += f"error gen in {l_num} line Typo in register name\n"
    elif ch==2:
        binary_ans += "1111000000"+reg_to_bin[i[1]]+reg_to_bin[i[2]]+"\n"
        
def var(l):
    c=0
    global opcode
    l = l.split()
    if(len(l)==2):
        if (l[1] == "FLAGS"): 
            c = 1
        elif (l[1] in opcode):
            c = 5
        elif (l[1] in reg_to_bin2):
            c =2
        elif (l[1] in loop.keys()):
            c = 3
        else:
            c = 4
    var_converter(l, c)

def movf(l):
    c =0
    l = l.split()
    if (len(l) == 3):
        if (l[1] == "FLAGS" or l[2] == "FLAGS"):
            c = 1
        elif (l[1] in reg_to_bin2):
            if (l[2][0] == "$"):
                c=2
            else:
                c = 5
        else:
            c =6
    movf_converter(l, c)


def add(l):
    k=0
    c = 0
    l = l.split()
    if(l[0] == "addf"):
        k=1
    if (len(l)==4):
        if (l[1] == "FLAGS" or l[2] == "FLAGS" or l[3] == "FLAGS"):
            c = 1
        elif (l[1]  in reg_to_bin2 and l[2]  in reg_to_bin2 and l[3]  in reg_to_bin2):
            c = 2
        else:
            c = 3
    add_converter(l,c,k)




def sub(l):
    k=0
    c = 0
    l = l.split()
    if(l[0] == "subf"):
        k=1
    if (len(l)==4):
        if (l[1] == "FLAGS" or l[2] == "FLAGS" or l[3] == "FLAGS"):
            c = 1
        elif ( l[1]  in reg_to_bin2 and l[2]  in reg_to_bin2 and l[3]  in reg_to_bin2):
            c = 2
        else:
            c = 3
    sub_converter(l,c,k)

def mul(l):
    c = 0
    l = l.split()
    if (len(l)==4):
        if (l[1] == "FLAGS" or l[2] == "FLAGS" or l[3] == "FLAGS"):
            c = 1
        elif ( l[1]  in reg_to_bin2 and l[2]  in reg_to_bin2 and l[3]  in reg_to_bin2):
            c = 2
        else:
            c =3
    mul_converter(l,c)

def xor(l):
    c = 0
    l = l.split()
    if (len(l) == 4):
        if (l[1] == "FLAGS" or l[2] == "FLAGS" or l[3] == "FLAGS"):
                c = 1
        elif ( l[1]  in reg_to_bin2 and l[2]  in reg_to_bin2 and l[3]  in reg_to_bin2):
            c = 2
        else:
            c =3
    xor_converter(l,c)

def orr(l):
    c = 0
    l = l.split()
    if (len(l) == 4):
        if (l[1] == "FLAGS" or l[2] == "FLAGS" or l[3] == "FLAGS"):
                c = 1
        elif ( l[1]  in reg_to_bin2 and l[2]  in reg_to_bin2 and l[3]  in reg_to_bin2):
            c = 2
        else:
            c =3
    orr_converter(l,c)


def andd(l):
    c = 0
    l = l.split()
    if (len(l) == 4):
        if (l[1] == "FLAGS" or l[2] == "FLAGS" or l[3] == "FLAGS"):
                c = 1
        elif ( l[1]  in reg_to_bin2 and l[2]  in reg_to_bin2 and l[3]  in reg_to_bin2):
            c = 2
        else:
            c =3
    andd_converter(l,c)


def div(l):
    c = 0
    l = l.split()
    if (len(l) == 3):
        if (l[1] == "FLAGS" or l[2] == "FLAGS" ):
            c = 1
        elif ( l[1]  in reg_to_bin2 and l[2]  in reg_to_bin2 ):
            c = 2
        else:
            c =3
    div_converter(l,c)


def nott(l):
    c =0
    l = l.split()
    if (len(l) == 3):
        if (l[1] == "FLAGS" or l[2] == "FlAGS" ):
                c = 1
        elif ( l[1]  in reg_to_bin2 and l[2]  in reg_to_bin2 ):
            c = 2
        else:
            c =3
    nott_converter(l,c)

def cmpp(l):
    c =0
    l = l.split()
    if (len(l) == 3):
        if (l[1] == "FLAGS" or l[2] == "FlAGS" ):
                c = 1
        elif ( l[1]  in reg_to_bin2 and l[2]  in reg_to_bin2 ):
            c = 2
        else:
            c =3
    cmp_converter(l,c)

def movl(l):
    c =0
    l = l.split()
    if (len(l) == 3):
        if (l[1] == "FLAGS" or l[2] == "FLAGS"):
            c = 1
        elif (l[1] in reg_to_bin2):
            if (l[2][0] == "$"):
                if (l[2][1:].isdigit()):
                    if (int(l[2][1:]) > 0 and int(l[2][1:]) < 256):
                        c = 2
                    else:
                        c = 3
                else:
                    c =4
            else:
                c = 5
        else:
            c =6
    mov1_converter(l,c)

def mov2(l):
    c =0
    l = l.split()
    if (len(l) == 3):
       
        if (l[1] in reg_to_bin2 and l[2] in reg_to_bin2):
            c = 2
        elif (l[1] == "FLAGS" or l[2] in reg_to_bin2):
            c = 5
        elif (l[1] == reg_to_bin2 or l[2] in "FLAGS"):
            c =6
        else:
            c =3
    else:
        c =4
    mov2_converter(l, c)

def rs(l):
    c =0
    l = l.split()
    if (len(l) == 3):
        if (l[1] == "FLAGS" or l[2] == "FLAGS"):
            c = 1
        elif (l[1] in reg_to_bin2):
            if (l[2][0] == "$"):
                if (l[2][1:].isdigit()):
                    if (int(l[2][1:]) > 0 and int(l[2][1:]) < 256):
                        c = 2
                    else:
                        c = 3
                else:
                    c =4
            else:
                c = 5
        else:
            c =6
    rs_converter(l,c)

def ls(l):
    c =0
    l = l.split()
    if (len(l) == 3):
        if (l[1] == "FLAGS" or l[2] == "FLAGS"):
            c = 1
        elif (l[1] in reg_to_bin2):
            if (l[2][0] == "$"):
                if (l[2][1:].isdigit()):
                    if (int(l[2][1:]) > 0 and int(l[2][1:]) < 256):
                        c = 2
                    else:
                        c = 3
                else:
                    c =4
            else:
                c = 5
        else:
            c =6
    ls_converter(l,c)

def ld(l):
    c = 0
    l = l.split()
    if(len(l) == 3):
        if (l[1] == "FLAGS" or l[2] == "FLAGS"):
            c =1
        elif(l[1] in reg_to_bin2):
            if(l[2] in gvariables.keys()):
                c = 2
            elif (l[2] in loop.keys()):
                c= 3
            else:
                c =4
        else:
            c = 5
    
    ld_converter(l, c)

def st(l):
    c = 0
    l = l.split()
    if(len(l) == 3):
        if (l[1] == "FLAGS" or l[2] == "FLAGS"):
            c =1
        elif(l[1] in reg_to_bin2):
            if(l[2] in gvariables.keys()):
                c = 2
            elif (l[2] in loop.keys()):
                c= 3
            else:
                c =4
        else:
            c = 5
    st_converter(l, c)

def jmp(l):
    c = 0
    l = l.split()
    if (len(l) == 2):
        if (l[1] in loop.keys()):
            c = 1
        elif (l[1] in gvariables.keys()):
            c = 2
        else:
            c = 3
    jmp_converter(l,c)

def jlt(l):
    c =0
    l = l.split()
    if (len(l) == 2):
        if (l[1] in loop.keys()):
            c = 1
        elif (l[1] in gvariables.keys()):
            c = 2
        else:
            c = 3
    jlt_converter(l,c)

def jgt(l):
    c=0
    l = l.split()
    if (len(l) == 2):
        if (l[1] in loop.keys()):
            c = 1
        elif (l[1] in gvariables.keys()):
            c = 2
        else:
            c = 3
    jgt_converter(l,c)
    
def je(l):
    c =0
    l = l.split()
    if (len(l) == 2):
        if (l[1] in loop.keys()):
            c = 1
        elif (l[1] in gvariables.keys()):
            c = 2
        else:
            c = 3
    je_converter(l,c)

def label(l):
    global check
    global error 
    global l_num
    l = l.split()
    if(len(l) >= 2 ):
        input_checker([" ".join(l[1:])])
    else:
        check = 1
        l_num = l_num+1
        error += f"error gen in {l_num} line General syntax error\n"
    
def hlt(l):
    c =0
    l = l.split()
    if(len(l) == 1):
        c = 1
    hlt_converter(l,c)

def hlt2(l):
    c =0
    l = l.split()
    if(len(l) == 2):
        c = 1
    hlt_converter2(l,c)

def not_present():
    global error
    global check
    check = 1
    error+=f"error gen in {l_num} line Typos in instruction name\n"

def check_hlt():
    global check
    global inp
    global error
    global l_num 
    if (inp[l_num-1] == "hlt" or inp[l_num-1] == f"{inp[l_num-1].split()[0]} hlt"):
        pass
    else:
        check = 1
        error += f"error gen missing hlt instruction\n"

def input_checker(inp):
    if (len(inp)==0):
        exit()
    global l_num
    global check
    global error
    global var_count
    for i in inp:
        l_num = l_num +1
        if (len(i) == 0):
            continue
        elif i.split()[0]=="var":
            if (l_num <= var_count):
                var(i)
            else:
                check =1
                error += f"error gen in {l_num} line variables not declared at the beginning\n"
        elif i.split()[0]=="mov":
            if i.split()[2][0]=="$":
                movl(i)
            else:
                mov2(i)
        elif i.split()[0]=="movf":
            movf(i)
        elif i.split()[0]=="add" or i.split()[0]=="addf":
            add(i)
        elif i.split()[0]=="sub" or i.split()[0]=="subf":
            sub(i)
        elif i.split()[0]=="ld":
            ld(i)
        elif i.split()[0]=="st":
            st(i)
        elif i.split()[0]=="mul":
            mul(i)
        elif i.split()[0]=="div":
            div(i)
        elif i.split()[0]=="rs":
            rs(i)
        elif i.split()[0]=="ls":
            ls(i)
        elif i.split()[0]=="xor":
            xor(i)
        elif i.split()[0]=="or":
            orr(i)
        elif i.split()[0]=="and":
            andd(i)
        elif i.split()[0]=="not":
            nott(i)
        elif i.split()[0]=="cmp":
            cmpp(i)
        elif i.split()[0]=="jmp":
            jmp(i)
        elif i.split()[0]=="jlt":
            jlt(i)
        elif i.split()[0]=="jgt":
            jgt(i)
        elif i.split()[0]=="je":
            je(i)
        elif i.split()[0]=="hlt":
            if(l_num < len(inp)):
                check = 1
                error += f"error gen in {l_num} hlt not being used as last instruction\n"
            else:
                hlt(i)

        elif i.split()[0][-1]==":" and len(i.split())==1:
            check=1
            error+=f"error gen in {l_num} General syntax error\n"
        
        # elif len(i.split())>1:
        #     if i.split()[0][-1]==":" and i.split()[1] == "hlt":
        #         if(l_num < len(inp)):
        #             check = 1
        #             error += f"error gen in {l_num} hlt not being used as last instruction\n"
        #         else:
        #             hlt2(i)
        
        elif i.split()[0][-1]==":" :
            the=0
            if len(i.split())>1:
                if i.split()[0][-1]==":" and i.split()[1] == "hlt":
                    the=1
                    if(l_num < len(inp)):
                        check = 1
                        error += f"error gen in {l_num} hlt not being used as last instruction\n"
                    else:
                        hlt2(i)
            if(i.split()[0][:-1] in opcode):
                check = 1
                error += f"error gen in {l_num} General syntax error\n"
            else:
                if the==0:
                    try:
                        if i.split()[1][-1]==":" :
                            check = 1
                            error += f"error gen in {l_num} line misuse of label\n"
                        else:
                            l_num = l_num -1
                            label(i) 
                    except Exception as e:
                        l_num = l_num -1
                        label(i)
        else:
            not_present()

def input_converter():
    a=[]
    b=[]
    for line in sys.stdin:
        a.append(line)

    for i in range(0, len(a)):
        temp=" ".join(a[i].split())
        b.append(temp)

    b.reverse()
    i=0
    while i<len(a):
        if b[i]=='':
            i += 1
        else:
            break

    for j in range(i, len(a)):
        inp.append(b[j])
    inp.reverse()
    


input_converter()
label_counter()
var_counter()
count_no_var()
good_variable()
input_checker(inp)

if check==1:
    check_hlt()
    for i in error:
        if i=='\n':
            break
        else:
            print(i, end='')
    print("\n")
else:
    check_hlt()
    if (check == 1):
        for i in error:
            if i=='\n':
                break
            else:
                print(i, end='')
        print("\n")
    else:
        print(binary_ans)