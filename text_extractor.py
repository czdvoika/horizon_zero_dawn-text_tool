import sys
s = open(sys.argv[2], "w", encoding = "utf-8")
f = open(sys.argv[1],"rb",)
i = 1
off = 0
textak = f.read()

while i < 999: 
 pozice1 = textak.find(b"\xE2\xB2\x0B\x42\x6B\x59\x9A\xB8", off)
 offset = f.seek(pozice1+28) 
 size = f.read(2)
 langsize = int.from_bytes(size,byteorder="little")
 text = (f.read(langsize))
 finish = text.decode('utf-8')
 enko = finish.replace("\n","\\n")
 s.write(enko)
 print(enko)
 s.write("\n")
 off = offset
 i += 1
  
s.close()
f.close() 
