s = open("save_trans.txt", "r", encoding = "utf-8" )
f = open("simpletext_pc.core", "r+b")
i = 1
k = 1
off = 0
textak = f.read()

while k < 822:
 pozice1 = textak.find(b"\xE2\xB2\x0B\x42\x6B\x59\x9A\xB8",off)
 offset = f.seek(pozice1+28)
 text = s.readline()
 encodetext = text.encode("utf-8")
 i = 1

 while i <22:
  lang1 = f.read(2)
  print(lang1)
  lang1 = int.from_bytes(lang1,byteorder="little")
  print(lang1)
  start1 = f.tell()
  print(start1)
  end1 = f.seek(start1+lang1)
  print(end1)
  i += 1

 offoffset = offset+2
 print(offoffset)
 print(end1)

 blok = (end1 - offoffset)
 print(blok)
 f.seek(offoffset)
 print(f.tell())

 f.write(b" "*blok)
 f.seek(offoffset)
 f.write(encodetext[:-1])
 endtext = f.tell()
 print(endtext)

 sizetext = (endtext - offoffset)
 hex(sizetext)
 enusize = sizetext.to_bytes(2, 'little')
 print(sizetext)
 print(enusize)
 f.seek(offset)
 f.write(enusize)
 f.seek(endtext)
 f.write(b"\x02\x00\x20\x20"*17)
 f.write(b"\x00\x00\x02\x00\x20\x20")

 konecnull = f.tell()
 print(konecnull)


 koneclang = (end1 - konecnull - 2)
 print(koneclang)

 hex(koneclang)
 konecek = koneclang.to_bytes(2, 'little')
 print(konecek)
 f.write(konecek)
 off = offset
 k += 1
 i == 1


s.close()
f.close()
