from math import sqrt; from itertools import count, islice
import random
def is_Prime(n):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n!=int(n):
        return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
 
    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
 
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(80):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True  
import gmpy
f= open("pDetail","r")
cont = f.read()
n = int(cont,16)
print(n)
print("------\n")

pF = open("prime.txt","r")
pFc = pF.read()
pFc = pFc.replace("\n","")
pFc = pFc.replace(" ","")

pFc = pFc.replace(":","")
pFc = pFc.replace("\r","")

p= int (pFc,16)
print("p is "+str(p))


print("------\n")

e = 65537
#temp exec
#p =17
#n = 187
#e = 7


##trasnvrt 



q = n // p
print("n is :")
print (q*p == n)
exit()

#p2=p
#q2=q

#p=q2
#q=p2


print(q)
print("------\n")


phi = (p-1)*(q-1)

m = phi

d = gmpy.invert(e,m)
print(d)

e1 = d % (p-1)
e2 = d %(q-1)
coef = gmpy.invert(q,p)

print("e1 : "+str(e1))

print("e2 : "+str(e2))

print("coef"+str(coef))


mP="asn1=SEQUENCE:rsa_key\n"
mP=mP+"\n"
mP=mP+"[rsa_key]\n"
mP=mP+"version=INTEGER:0\n"
mP=mP+"modulus=INTEGER:"+str(n)+"\n"
mP=mP+"pubExp=INTEGER:"+str(e)+"\n"
mP=mP+"privExp=INTEGER:"+str(d)+"\n"
mP=mP+"p=INTEGER:"+str(p)+"\n"
mP=mP+"q=INTEGER:"+str(q)+"\n"
mP=mP+"e1=INTEGER:"+str(e1)+"\n"
mP=mP+"e2=INTEGER:"+str(e2)+"\n"
mP=mP+"coeff=INTEGER:"+str(coef)+"\n"

print(mP)

f = open ("privkey.asn","w")
f.write(mP)
