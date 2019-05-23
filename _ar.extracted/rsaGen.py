

def gcd(a, b):
    # Return the GCD of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    # Returns the modular inverse of a % m, which is
    # the number x such that a*x % m = 1

    if gcd(a, m) != 1:
        return None # no mod inverse if a & m aren't relatively prime

    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m



# RSA Key Generator
# http://inventwithpython.com/hacking (BSD Licensed)

import random, sys, os


def main():
    # create a public/private keypair with 1024 bit keys
    print('Making key files...')
    makeKeyFiles('al_sweigart', 4096)
    print('Key files made.')

def generateKey(keySize):
    # Creates a public/private key pair with keys that are keySize bits in
    # size. This function may take a while to run.

    # Step 1: Create two prime numbers, p and q. Calculate n = p * q.
    print('Generating p prime...')
    p = 16064248597663569810455542995795706120645942243795146455321838731239581169897755090529933604542872726173944827074931411323520631009175683977900670399850100874046521780006947997023417800554140183787098974849794621275093181301655098818085357647914638532519622092141656406463115592261391094745818640153314794869659797307832118274716885917436862462589823358083713178386183669067102140391617572744686310402118326043859642857610837008158858832453970265920726817763377522527207581327514809799386420687936851423622531026421363275265742044514925429667733259946364214019019764853989926493351408587088329537546088834022901514005

    print('Generating q prime...')
    q = 52156162721753602693937611214135773169718103067834030215772881077266041767272308486232378857849258332809705554626907449142397598165918189376587664413559878374405777300340875623691509821763206433096477877628490990646721861923479425586277344236236352298306175492448601227295177021206405086917019519765345174573717242394403218989114547170980436861243674309001783164445639068245602224140772989872800268369023658618010677650385937847033778215948774438882765970780245206546749941279527434308876005021940767882030816740216709073048208783008324032507641185537584449405072634701743050260669339370461134296880720075372199175862
    n = p * q

    # Step 2: Create a number e that is relatively prime to (p-1)*(q-1).
    print('Generating e that is relatively prime to (p-1)*(q-1)...')
    while True:
        # Keep trying random numbers for e until one is valid.
        e = 65537
        if gcd(e, (p - 1) * (q - 1)) == 1:
            break

    # Step 3: Calculate d, the mod inverse of e.
    print('Calculating d that is mod inverse of e...')
    d = findModInverse(e, (p - 1) * (q - 1))

    publicKey = (n, e)
    privateKey = (n, d)

    print('Public key:', publicKey)
    print('Private key:', privateKey)

    return (publicKey, privateKey)


def makeKeyFiles(name, keySize):
    # Creates two files 'x_pubkey.txt' and 'x_privkey.txt' (where x is the
    # value in name) with the the n,e and d,e integers written in them,
    # delimited by a comma.

    # Our safety check will prevent us from overwriting our old key files:
    if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists('%s_privkey.txt' % (name)):
        sys.exit('WARNING: The file %s_pubkey.txt or %s_privkey.txt already exists! Use a different name or delete these files and re-run this program.' % (name, name))

    publicKey, privateKey = generateKey(keySize)

    print()
    print('The public key is a %s and a %s digit number.' % (len(str(publicKey[0])), len(str(publicKey[1]))))
    print('Writing public key to file %s_pubkey.txt...' % (name))
    fo = open('%s_pubkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
    fo.close()

    print()
    print('The private key is a %s and a %s digit number.' % (len(str(publicKey[0])), len(str(publicKey[1]))))
    print('Writing private key to file %s_privkey.txt...' % (name))
    fo = open('%s_privkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
    fo.close()


# If makeRsaKeys.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()

