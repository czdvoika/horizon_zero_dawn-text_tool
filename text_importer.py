import sys
s = open(sys.argv[1], "r", encoding = "utf-8" )
f = open(sys.argv[2], "r+b")
i = 1
k = 0
off = 0
m = 1
textak = f.read()
kolik = textak.count(b"\xE2\xB2\x0B\x42\x6B\x59\x9A\xB8")

while k < kolik:
 pozice1 = textak.find(b"\xE2\xB2\x0B\x42\x6B\x59\x9A\xB8",off)
 offset = f.seek(pozice1+28)
 text = s.readline().replace("\\n",chr(10))
 encodetext = text.encode("utf-8")
 i = 1

 while i <22:
  lang1 = f.read(2)
  # print(lang1)
  lang1 = int.from_bytes(lang1,byteorder="little")
  # print(lang1)
  start1 = f.tell()
  # print(start1)
  end1 = f.seek(start1+lang1)
  # print(end1)
  i += 1

 print("---------------------")
 offoffset = offset+2
 print(offoffset)
 print(end1)

 blok = (end1 - offoffset)
 print("blok: ",blok)
 f.seek(offoffset)
 print(f.tell())

 if blok < 31000:
 
  f.write(b"\x00"*blok)
  f.seek(offoffset)
  f.write(encodetext[:-1])
  endtext = f.tell()
  print(endtext)
 
  sizetext = (endtext - offoffset)
  print("sizetext: ",sizetext)
  hex(sizetext)
  enusize = sizetext.to_bytes(2, 'little')
  print("textsize: ",sizetext)
  print("enusize: ",enusize)
  f.seek(offset)
  f.write(enusize)
  f.seek(endtext)
  f.write(b"\x00\x00"*19)
  
 
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
  
 elif blok: 
  print("kokokokokokokokokokokokokokokokot")
  f.write(b"\x00"*blok)
  f.seek(offoffset)
  f.write(encodetext[:-1])
  endtext = f.tell()
  print(endtext)
 
  sizetext = (endtext - offoffset)
  print("sizetext: ",sizetext)
  hex(sizetext)
  enusize = sizetext.to_bytes(2, 'little')
  print("textsize: ",sizetext)
  print("enusize: ",enusize)
  f.seek(offset)
  f.write(enusize)
  f.seek(endtext)
  blok_deleno = round(blok/18)
  print("deleno 18:  ",blok_deleno)
  
  
  m = 0
  
  while m < 16:
   print("kdejsem",f.tell())
   offdeleno = f.tell()
   hex(blok_deleno)
   konecek2 = blok_deleno.to_bytes(2, 'little')
   print("konecek2:",konecek2)
   f.write(konecek2)
   f.seek(offdeleno+blok_deleno+2)
   m += 1
 
  
  
  
  konecnull = f.tell()
  print(konecnull)
 
 
  koneclang = (end1 - konecnull - 2)
  print(koneclang)
 
  off = offset
  k += 1
  i == 1
  m == 1


s.close()
f.close()








































































