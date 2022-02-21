fh = open("more.core", "r+b")
bin = fh.read()
pozice1 = bin.find(b"\xE2\xB2\x0B\x42\x6B\x59\x9A\xB8")
print(pozice1)
text = fh.seek(pozice1+28)
print(text)
size = fh.read(1)
nic = fh.read(1)
fh.write(b"picak")


fh.close()
