import sys
pc = -1
inp1 = []
flg="0000000000000000"
flagv=0
flagl=0
flagg=0
flage=0

string="00000000"

variab = {}
lab = []

for line in sys.stdin:
    inp1.append(line)

inp=[]

for i in inp1:
    if(i=="" or i==" " or i=="\n"):
        continue
    else:
        inp.append(i)

if inp[-1][-1]!="\n":
    inp[-1]=inp[-1]+"\n"

for i in inp:
    if i[0:5] == "10101":
        variab[i[8:16]] = 0
        
# for i in inp:
#     if i[0:5] == "11111" or i[0:5] == "01100" or i[0:5] == "01101" or i[0:5] == "01111":
#         lab.append(i[8:16])


 
def bintodeci(n):
    l=[]
    for alpha in n:
        if(alpha != "\n"):
            l.append(alpha)
    l.reverse()
    sum=0
    for i,j in enumerate(l):
        sum+=(2**int(i))*int(j)
    return sum

def decitobin2(num):
    c=0
    d = 0
    for i in str(num):
        if i == ".":
            c = 1
            d += 1
    if c == 1:
        whole_list = []
        dec_list = []
        places=8
        whole, dec = str(num).split('.')
        whole = int(whole)
        dec = int(dec)
        counter = 1

        while (whole / 2 >= 1):
                i = int(whole % 2)
                whole_list.append(i)
                whole /= 2
                
        decproduct = dec      
        while (counter <= places):
            decproduct = decproduct * (10**-(len(str(decproduct))))
            decproduct *= 2
            decwhole, decdec = str(decproduct).split('.')
            decwhole = int(decwhole)
            decdec = int(decdec)
            dec_list.append(decwhole)
            decproduct = decdec
            counter += 1
                

        whole_list.insert(0,1)

        for i in range(8-len(whole_list)):
            whole_list.insert(0,0)

        for i in range(len(whole_list)):
            whole_list[i]=str(whole_list[i])

        for i in range(len(dec_list)):
            dec_list[i]=str(dec_list[i])  
        whole_string= "".join(whole_list)
        dec_string= "".join(dec_list)
        final_string=whole_string + dec_string
        return final_string
        
    n=int(num)
    if n==0:
        return "0000000000000000"
    else:
        l=[]
        while n!=0:
            l.append(str(n%2))
            n//=2
        while len(l)<16:
            l.append("0")
        l.reverse()
        return ''.join(l)


def decitobin1(n):
    n=int(n)
    if n==0:
        return "00000000"
    else:
        l=[]
        while n!=0:
          
            l.append(str(n%2))
            n//=2
        while len(l)<8:
            l.append("0")
        l.reverse()
        return ''.join(l)


def floatconverter(n):
    a = n[0:4]
    b = n[4:8]
    c = bintodeci(a)
    lent = len(b)
    sum = 0
    for i in range(0,lent,1):
        sum = sum + 2**(-1*(i+1))*int(b[i])
    e = c+sum
    return str(e)

regval = {
    "000" : 0,
    "001" : 0,
    "010" : 0,
    "011" : 0,
    "100" : 0,
    "101" : 0,
    "110" : 0,
    # "111" : "0000000000000000"
}



def setzero():
    global flg
    a=list(flg)
    a[-1]="0"
    a[-2]="0"
    a[-3]="0"
    a[-4]="0"
    a[-5]="0"
    a[-6]="0"
    a[-7]="0"
    b = ''.join(a)
    flg = b



def printvalues():
    global flg
    print(decitobin1(pc),decitobin2(regval["000"]),decitobin2(regval["001"]),decitobin2(regval["010"]),decitobin2(regval["011"]),decitobin2(regval["100"]),decitobin2(regval["101"]),decitobin2(regval["110"]),flg)

def printcounter():
    global flg
    global pc
    print(decitobin1(pc),decitobin2(regval["000"]),decitobin2(regval["001"]),decitobin2(regval["010"]),decitobin2(regval["011"]),decitobin2(regval["100"]),decitobin2(regval["101"]),decitobin2(regval["110"]),flg)
   

while(True):
    pc += 1
    #add
    if(inp[pc][0:5]=="10000"):
        setzero()
        regval[inp[pc][13:16]] = regval[inp[pc][10:13]] + regval[inp[pc][7:10]]
        if(regval[inp[pc][13:16]]>=256): 
           
            a=list(flg)
            a[-4] = "1"
            b = ''.join(a)
            flg = b
        
        printvalues()
        

    #addf
    if(inp[pc][0:5]=="00000"):
        setzero()
        regval[inp[pc][13:16]] = regval[inp[pc][10:13]] + regval[inp[pc][7:10]]
        if(regval[inp[pc][13:16]]>=256): 
           
            a=list(flg)
            a[-4] = "1"
            b = ''.join(a)
            flg = b
        printvalues()
        

    #sub
    elif(inp[pc][0:5]=="10001"):
        setzero()
        if(regval[inp[pc][10:13]] > regval[inp[pc][7:10]]):
            regval[inp[pc][13:16]]=0
            a=list(flg)
            a[-4] = "1"
            b = ''.join(a)
            flg = b
        else:
            regval[inp[pc][13:16]] = regval[inp[pc][7:10]] - regval[inp[pc][10:13]] 
        
        printvalues()
        

    #subf
    elif(inp[pc][0:5]=="00001"):
        setzero()
        # print(1)
        if(regval[inp[pc][10:13]] > regval[inp[pc][7:10]]):
            regval[inp[pc][13:16]]=0
            a=list(flg)
            a[-4] = "1"
            b = ''.join(a)
            flg = b
        else:
            regval[inp[pc][13:16]] = regval[inp[pc][7:10]] - regval[inp[pc][10:13]] 
        printvalues()
        
            

    #mul
    elif(inp[pc][0:5]=="10110"):
        setzero()
        regval[inp[pc][13:16]] = regval[inp[pc][10:13]] * regval[inp[pc][7:10]]
        # print(regval[inp[pc][13:16]])
        if(regval[inp[pc][13:16]]>=256):
            a=list(flg)
            a[-4] = "1"
            b = ''.join(a)
            flg = b
            
        # print(3)
        printvalues()
        
    #xor
    elif(inp[pc][0:5]=="11010"):
        setzero()
        regval[inp[pc][13:16]] = regval[inp[pc][10:13]] ^ regval[inp[pc][7:10]]
        
        # print(4)
        printvalues()
    #or
    elif(inp[pc][0:5]=="11011"):
        setzero()
        regval[inp[pc][13:16]] = regval[inp[pc][10:13]] | regval[inp[pc][7:10]]
        
        
        # print(5)
        printvalues()

    #and
    elif(inp[pc][0:5]=="11100"):
        setzero()
        regval[inp[pc][13:16]] = regval[inp[pc][10:13]] & regval[inp[pc][7:10]]
        # print(6)
        printvalues()

    #divide
    elif(inp[pc][0:5]=="10111"):
        setzero()
        regval["000"] = int(regval[inp[pc][10:13]] / regval[inp[pc][13:16]])
        regval["001"] = regval[inp[pc][10:13]] % regval[inp[pc][13:16]]
        
        # print(8)
        printvalues()

    # #not
    # elif(inp[pc][0:5]=="11101"):
    #     setzero()
    #     regval[inp[pc][13:16]] =  not(regval[inp[pc][10:13]])
    #     # print(0)
    #     printvalues()

    #not
    elif(inp[pc][0:5]=="11101"):
        setzero()
        regval[inp[pc][13:16]] = 65535 - regval[inp[pc][10:13]] 
        # print(0)
        printvalues()

    #compare
    elif(inp[pc][0:5]=="11110"):
        setzero()
        if(regval[inp[pc][10:13]] < regval[inp[pc][13:16]]):
            a=list(flg)
            a[-3] = "1"
            b = ''.join(a)
            flg = b
            flagl=1
        elif(regval[inp[pc][10:13]] == regval[inp[pc][13:16]]):
            a=list(flg)
            a[-1] = "1"
            b = ''.join(a)
            flg = b
            flage=1
        elif(regval[inp[pc][10:13]] > regval[inp[pc][13:16]]):
            a=list(flg)
            a[-2] = "1"
            b = ''.join(a)
            flg = b
            flagg=1
            
            
        # print(10)
        printvalues()
    #mov immediate
    elif(inp[pc][0:5]=="10010"):
        setzero()
        regval[inp[pc][5:8]] = bintodeci(inp[pc][8:])
        # print(11)
        printvalues()

    #mov fimmediate
    elif(inp[pc][0:5]=="00010"):
        setzero()
        regval[inp[pc][5:8]] = float(floatconverter(inp[pc][8:]))
        printvalues()
        
    
    #right shift
    elif(inp[pc][0:5]=="11000"):
        setzero()
        regval[inp[pc][5:8]] = regval[inp[pc][5:8]] >> bintodeci(inp[pc][8:])
        # print(19)
        printvalues()

    #left shift
    elif(inp[pc][0:5]=="11001"):
        setzero()
        regval[inp[pc][5:8]] = regval[inp[pc][5:8]] << bintodeci(inp[pc][8:])
        printvalues()

    #mov reg
    elif(inp[pc][0:5]=="10011"):
        if inp[pc][10:13] == "111":
            regval[inp[pc][13:16]] = bintodeci(flg)
            setzero()
        else:
            setzero()
            regval[inp[pc][13:16]] = regval[inp[pc][10:13]]
        printvalues()

        # regval[inp[pc][13:16]] = regval[inp[pc][10:13]]
        # printvalues()
        # setzero()
    
    #hlt
    elif(inp[pc][0:5]=="01010"):
        # setzero()
        
        # print(98)
        printvalues()
        break
    
    #load
    elif(inp[pc][0:5]=="10100"):
        setzero()
        regval[inp[pc][5:8]] = variab[inp[pc][8:16]]
        printvalues()
        

    #store
    elif(inp[pc][0:5]=="10101"):
        setzero()
        variab[inp[pc][8:16]] = regval[inp[pc][5:8]]
        printvalues()


    #unconditional jump (jmp)
    elif(inp[pc][0:5]=="11111"):  
        setzero()   
        printcounter()
        pc=bintodeci(inp[pc][5:])-1
        # setzero()
        # print(pc)
        
    #jump if less than (jlt)
    elif(inp[pc][0:5]=="01100"):
        setzero()
        printcounter()
        if(flagl==1):
            pc=bintodeci(inp[pc][5:])-1
            # print(18)
        flagl=0
        # setzero()

    #jump if greater than (jgt)
    elif(inp[pc][0:5]=="01101"):
        setzero()
        printcounter()
        if(flagg==1):
            pc=bintodeci(inp[pc][5:])-1
        # print(44)
        flagg=0
        # setzero()
        
    #jump if equal (je)
    elif(inp[pc][0:5]=="01111"):
        setzero()
        printcounter()
        if(flage==1):
            pc=bintodeci(inp[pc][5:])-1
            # print(pc)
        flage=0
        # setzero()

for i in inp:
    print(i[:-1])

mem=dict(reversed(list(variab.items())))

for i in mem.keys():
    # zero="0"*8
    # zero+=i
    print(decitobin2(mem[i]))


num = 256 - len(inp) - len(variab)

for i in range(num):
    print("0000000000000000")