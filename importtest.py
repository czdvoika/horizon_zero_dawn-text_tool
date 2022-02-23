core = open("simpletext_slovak.core", "rb")
txt =  open("save.txt", "r")
binar = core.read()
line = txt.readline()

binline = line.encode("utf-8")
print(binline)
size = len(binline)
nsize = (size-1)
print(nsize)
usize = chr(nsize)
print(usize)


pozice1 = binar.find(b"\xE2\xB2\x0B\x42\x6B\x59\x9A\xB8")
print(pozice1)
offset = core.seek(pozice1+28)
print(offset)
