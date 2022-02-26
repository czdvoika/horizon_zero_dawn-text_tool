s = open("save_czech.txt", "r", encoding = "utf-8" )
f = open("simpletext_pc.core", "r+b")
i = 1
off = 0
textak = f.read()

while i < 823: 
 pozice1 = textak.find(b"\xE2\xB2\x0B\x42\x6B\x59\x9A\xB8", off)
 offset = f.seek(pozice1+28)

 line = s.readline()
 print(line)
 start = f.tell()
 print("start",f.tell())

 encodeline = line.encode("utf-8")
 f.write(b"..")
 f.write(encodeline)
 end = f.tell()
 print("end",f.tell())
 f.write(b'\x02')

 sizeoff = (end - start - 2)
 print(sizeoff)

 usize = hex(sizeoff)
 print("hexsize",usize)

 enusize = sizeoff.to_bytes(2, 'little')
 print("hexsize",enusize)
 f.seek(start)
 f.write(enusize)
 
 print(start)

 off = offset
 i += 1

s.close()
f.close() 


