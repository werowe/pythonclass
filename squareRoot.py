a=2

a1 = a+1
b1 = a/a1
anminus1 = a1
bnminus1 = b1


while (anminus1-bnminus1 > 0):
    an = 0.5 * (anminus1 + bnminus1)
    bn = a / an
    anminus1 = an
    bnminus1 = bn
    print(an,bn,an-bn)

