with open('save.txt', encoding='utf8') as text:
 line = text.readline()
 print(line)
 size = len(line)
 nsize = (size-1)
 print(nsize)
 hexsize = hex(nsize)
 print(hexsize)
 hotovo = hexsize.replace("0x","\\x")
 print(hotovo)
 

with open('save.core', 'w') as save:
 
 save.write(hotovo)

# [2:]
# core = open("simpletext_pc.core", "rb")
# txt =  open("save.txt", "r", "utf-8")

# line = txt.readline()
# print(line)

# print(binline)
# size = len(binline)
# nsize = (size-1)
# print(nsize)

# char = chr(nsize)
# print(char)


# usize = chr(nsize)
# enusize = usize.encode("utf-8")
# print(enusize)
# hexsize = hex(nsize)
# print(hexsize)

# finish = usize.encode("utf-8")
# print(finish)

# pozice1 = binar.find(b"\xE2\xB2\x0B\x42\x6B\x59\x9A\xB8")
# print(pozice1)
# offset = core.seek(pozice1+28)
# print(offset)


