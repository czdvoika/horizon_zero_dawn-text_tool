s = open("save_czech.txt", "r", encoding = "utf-8" )
f = open("simpletext_pc.core", "r+b")
i = 1
off = 0
textak = f.read()

line = s.readline()
pozice1 = textak.find(b"\xE2\xB2\x0B\x42\x6B\x59\x9A\xB8", off)
offset = f.seek(pozice1+28)

while i <18:
 lang1 = f.read(2)
 lang1 = int.from_bytes(lang1,byteorder="little")
 start1 = f.tell()
 end1 = f.seek(start1+lang1)
 i += 1

print(offset)
print(end1)

f.seek(offset)
newsize = (end1 - offset)
f.write(b" "*newsize)
f.seek(offset+2)

print(f.tell())
encodeline = line.encode("utf-8")
f.write(encodeline)
print(encodeline)
konecsize = f.tell()
print(konecsize)
f.seek(offset)
print(offset)
writekonec = (konecsize - offset - 2)

hexwritesize = hex(writekonec)
print(hexwritesize)
enusize = writekonec.to_bytes(2, 'little')
f.write(enusize)
f.seek(konecsize)
f.write(b"\x02\x00\x20\x20\x02\x00\x20\x20\x02\x00\x20\x20\x02\x00\x20\x20\x02\x00\x20\x20\x02\x00\x20\x20\x02\x00\x20\x20\x02\x00\x20\x20\x02\x00\x20\x20\x02\x00\x20\x20\x02\x00\x20\x20\x02\x00\x20\x20\x02\x00\x20\x20\x02\x00\x20\x20\x02\x00\x20\x20")

posledni = f.tell()
print(posledni)
offoffset = (end1 - posledni - 2)
print(offoffset)

hexwritesize2 = hex(offoffset)
print(hexwritesize2)
enusize2 = offoffset.to_bytes(2, 'little')
f.write(enusize2)
