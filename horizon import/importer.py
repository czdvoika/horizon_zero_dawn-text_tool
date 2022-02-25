s = open("save.txt", "r")
f = open("save.core", "r+b")

line = s.readline()
print(line)
size = len(line)
print(size)
nsize = (size-1)
print(nsize)
usize = hex(nsize)
print(usize)
enusize = nsize.to_bytes(2, 'little')
print(enusize)
f.write(enusize)
encodeline = line.encode("utf-8")
f.write(encodeline)



