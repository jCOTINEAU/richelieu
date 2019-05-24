from math import sqrt; from itertools import count, islice
import random
import itertools
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


n=837849563862443268467145186974119695264713699736869090645354954749227901572347301978135797019317859500555501198030540582269024532041297110543579716921121054608494680063992435808708593796476251796064060074170458193997424535149535571009862661106986816844991748325991752241516736019840401840150280563780565210071876568736454876944081872530701199426927496904961840225828224638335830986649773182889291953429581550269688392460126500500241969200245489815778699333733762961281550873031692933566002822719129034336264975002130651771127313980758562909726233111335221426610990708111420561543408517386750898610535272480495075060087676747037430993946235792405851007090987857400336566798760095401096997696558611588264303087788673650321049503980655866936279251406742641888332665054505305697841899685165810087938256696223326430000379461379116517951965921710056451210314300437093481577578273495492184643002539393573651797054497188546381723478952017972346925020598375000908655964982541016719356586602781209943943317644547996232516630476025321795055805235006790200867328602560320883328523659710885314500874028671969578391146701739515500370268679301080577468316159102141953941314919039404470348112690214065442074200255579004452618002777227561755664967507

import re

permut = dict()
permut["fb"]="7f"
permut["66"]="e1"
permut["12"]="f4"
permut["54"]="16"
permut["57"]="a4"
permut["cd"]="b5"


primeF = open("prime.txt","r")
prime = primeF.read()

founds = []

fbs = [m.start() for m in re.finditer('fb', prime)]
six6s = [m.start() for m in re.finditer('66', prime)]
douzes = [m.start() for m in re.finditer('12', prime)]
cinq4 = [m.start() for m in re.finditer('54', prime)]
cinq7 = [m.start() for m in re.finditer('57', prime)]
cds = [m.start() for m in re.finditer('cd', prime)]

 
for p in fbs:
    founds.append("fb,"+str(p))
 
for p in six6s:
    founds.append("66,"+str(p))

for p in douzes:
    founds.append("12,"+str(p))

for p in cinq4:
    founds.append("54,"+str(p))

for p in cinq7:
    founds.append("57,"+str(p))

for p in cds:
    founds.append("cd,"+str(p))

t = 0
int rez = []
size = len(founds)
print("founds is of length"+str(size))

for i in range(0,size+1):
    permuts = list(itertools.combinations(founds,i))
    for perm in permuts:
        s = prime
        t = t +1
        for shift in perm:
            splits = shift.split(",")
            mod = splits[0]
            index = int(splits[1])
            s = s[:index] + permut[mod] + s[index + 2:]
        s=s.replace(":","")
        s=s.replace("\n","")
        myI = int(s,16)
        print(t)
        if is_Prime(myI):
            print("succes")
            rez.append[myI]
    
print (t)
zboui = 0
for i in rez:
    f = open("myI"+str(zboui),"w")
    f.write(str(i))
    zboui = zboui +1



