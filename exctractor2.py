s = open("save.txt", "w")
f = open("sentences.core","rb",)
i = 1
off = 0
textak = f.read()

while i < 100: 
  
  pozice1 = textak.find(b"\xE2\xB2\x0B\x42\x6B\x59\x9A\xB8", off)
  print(pozice1)
  offset = f.seek(pozice1+28) 
  print(f.tell())
  
  size = f.read(1)
  nic = f.read(1) 
  print(size)
  usize = ord(size)
  print(usize)
 
  text = (f.read(usize))
  finish = text.decode('ascii')
  print(finish)
  s.write(finish)
  s.write("\n")
  
  off += offset
  i += 1
 

 
 
 
 
