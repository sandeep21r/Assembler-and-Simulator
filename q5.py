import math as m
type_memory = {"Bits":"-3","Nibbles" : "-1" , "Byte" : "0"}
type_memory2 = {"Bits":"1","Nibbles" : "4" , "Byte" : "8"}
powerr = {"G" : 30,"M":20,"k" : 10} 

print("1. ISA and Instructions","\n2(a). SYSTEM Enhancement","\n2(b). How big the mememory\n")


query =input("enter the the query number: ")
space_memory = input("Memory Space: ")
memory_address = input("Memory Address Type(for word addressable type cpu): ")

if(memory_address == "cpu"):
    n = input("enter the size of word addressable Memory in bits: ")
    nn = n.split(" ")
    type_memory["cpu"] = nn[0]
else:
    type_memory["CPU"] = "0"
if(query == "1"):
    lenght_ints = input("Length of instruction in bits: ")
    length_register = input("length of register in bits: ")
    length1 = lenght_ints.split(" ")
    length2 = length_register.split(" ")
    length_ints = length1[0]
    length_register = length2[0]
    
    space = space_memory.split(" ")
   
    space_bytes = int(space[0])*(2**(powerr[space[1][0]]))

    if(space[1][1] == "b"):
        space_bytes = space_bytes/8
        
    
    space_bytes = int(m.log2(space_bytes))
    type = int(type_memory[memory_address])
    if(memory_address == "cpu"):
        type = type/8
        type = m.log2(type)
    min_bit = int(space_bytes - type)
    
    
    opcode = int(int(length_ints) - (min_bit + int(length_register)))
    filler = int(length_ints) - (opcode+2*int(length_register))
  
    max_intruction = 2**opcode
    max_registers = 2**int(length_register)
    print("Minimum bits to represent address: ",min_bit)
    print("Number of bits needed by opcode: ",opcode)
    print("Number of filler bits in Instruction type 2: ",filler)
    print("Maximum numbers of instructions this ISA can support: ",max_intruction)
    print("Maximum number of registers this ISA can support: ",max_registers)
    
elif (query == "2(a)"):
   
    
    space = space_memory.split(" ")
   
    space_bytes = int(space[0])*(2**(powerr[space[1][0]]))

    if(space[1][1] == "b"):
        space_bytes = space_bytes/8
        
    
    space_bytes = int(m.log2(space_bytes))
    type = int(type_memory[memory_address])
    if(memory_address == "cpu"):
        type = type/8
        type = m.log2(type)
   
    min_bit = space_bytes - type
   
    n = input("enter the size of word addressable Memory in bits: ")
    nn = n.split(" ")
    ma = int(int(nn[0])/8)
    nn[0] = m.log2(ma)
    type_memory["cpu"] = nn[0]
    ench = input("enchanced into(for word addressable memory type cpu): ")
    min = space_bytes
    type1 = int(type_memory[ench])

    min = min - type1

    dif = min - min_bit
    if(dif > 0):
        print(dif,"(",dif,"Pins required)")
    elif(dif < 0):
        print(dif,"(",dif*(-1),"Pins required)")
    else:
        print(dif,"No pins required and saved")
elif(query == "2(b)"):
    n = input("enter the size of word addressable Memory in bits: ")
    nn = n.split(" ")
    type_memory2["cpu"] = nn[0]
    pin = int(input("enter the address pins: "))
    mem = input("enter the memeory addressable type(for word addressable type cpu): ")
    ans = 2**pin
    ans = int(ans*int(type_memory2[mem])/8)
    ans = int(ans)
    print("Main Memory size: ",ans,"Byte")

else:
    print("wrong input")