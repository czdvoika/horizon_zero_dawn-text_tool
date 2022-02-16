f = open("sentences.core", "rb")
s = open("save.txt", "w")
textak = f.read()


i = 1
o = 0
while i < 10:
 
 print(o)
 
 pozice1 = textak.find(b"\xE2\xB2\x0B\x42\x6B\x59\x9A\xB8")
 print(pozice1)
 pozice2 = f.seek(pozice1+28)
 print(pozice2)
 offset1 = (textak[pozice2])
 print(offset1)
 pozice3 = (pozice1+30)
 print(pozice3)
 pozice4 = (pozice3+offset1)
 print(pozice4)
 text = (textak[pozice3:pozice4])
 finish = text.decode('ascii')
 print(finish)
 s.write(finish)
 
 
 o += 1 
 i += 1








