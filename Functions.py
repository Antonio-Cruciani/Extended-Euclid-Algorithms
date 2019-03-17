import math
import random
import binascii

#Algoritmo euclideo esteso
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
         return None  #modular inverse non esiste 
    else:
        return x % m

e=42509
n=37065996431314739809492902731211123768504208130572860840044210903210729069893
p = 183071862341995238936186594830928510633
q = 202466921771255139807658161990161340221
crypto_message = 25339981238161822593063579378000917841822341970578339926071325721264662075193

#calcolo phi
phi = (p-1)*(q-1)
#calcolo la chiave privata
d = modinv(e,phi)


#decripto il messaggio
decrypted = pow(crypto_message, d, n)


#converto il messaggio
binario = bin(decrypted)
print binario
n = int('0b1000010011101010110111101101110001000000011001000110000001100010011100000100001', 2)
print binascii.unhexlify('%x' % n)
