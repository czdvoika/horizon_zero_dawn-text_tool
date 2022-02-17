fh = open("more.core", "r+b")
fh.seek(4060)

fh.write(b"kokot")
fh.close()
