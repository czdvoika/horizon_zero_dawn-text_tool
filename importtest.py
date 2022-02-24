with open('save.txt', encoding='utf8') as text:
 line = text.readline()
 print(line)
 size = len(line)
 nsize = (size-1)
 print(nsize)
 hexsize = hex(nsize)
 print(hexsize)
 hexdec = hexsize.replace("0x","")
 print(hexdec)
 bytedec = bytearray.fromhex(hexdec)
 print(bytedec)
 

with open('save.core', 'r+b') as save:
 core = save.read()
 pozice1 = core.find(b"\xE2\xB2\x0B\x42\x6B\x59\x9A\xB8")
 print(pozice1)
 offset = save.seek(pozice1+28)
 print(offset)
 save.write(bytedec)
 text = save.seek(offset+2)
 print(text)
 text = line.encode("utf8")
 save.write(text)
 
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

