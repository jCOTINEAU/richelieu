f= open("pDetail","r")
cont = f.read();
cont = cont.replace("\n","")
cont = cont.replace(":","")
cont = cont.replace(" ","")
cont = cont.replace("\r","")
cont = cont.replace(" ","")

n = int(cont, 16)
print(n)
print("------\n")
outN = open("nOut","w")
outN.write(str(n))


pF = open("prime.txt","r")
pFc = pF.read()
pFc = pFc.replace("\n","")
pFc = pFc.replace(" ","")

pFc = pFc.replace(":","")
pFc = pFc.replace("\r","")

p= int (pFc,16)
print(p)

print("------\n")

q = n // p
print(q)
print("------\n")
