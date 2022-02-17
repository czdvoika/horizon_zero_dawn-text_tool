o = open("save.txt", "r")
s = open("save2.txt", "w")
radek1 = o.readline()
print(radek1)
s.write(radek1)

o.close()
s.close()
