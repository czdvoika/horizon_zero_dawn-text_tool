s = open("save.txt", "w")
f = open("menu.core","rb",)
i = 1
off = 0
textak = f.read()

while i < 100: 
  pozice1 = textak.find(b"\xE2\xB2\x0B\x42\x6B\x59\x9A\xB8", off)
  offset = f.seek(pozice1+28) 
  size = f.read(1)
  nic = f.read(1) 
  usize = ord(size) 
  text = (f.read(usize))
  finish = text.decode('utf-8')
  enko = finish.replace("\n","\\n")
  s.write(enko)
  print(enko)
  s.write("\n")
  off = offset
  i += 1
