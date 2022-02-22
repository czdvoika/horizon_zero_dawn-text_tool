core = open("mourek.core", "r+b")
txt =  open("save.txt", "r")


bin = core.read()
pozice1 = bin.find(b"\xE2\xB2\x0B\x42\x6B\x59\x9A\xB8")
print(pozice1)
text = core.seek(pozice1+28)
print(text)
size = core.read(1)
usize = ord(size)
print(usize)
nic = core.read(1)

radek = txt.readline()
radek = radek.replace("\n","")
finish = radek.encode('utf-8')


# a = len(radek)
# print(a)


print(finish)
core.write(finish)


core.close()
txt.close()
