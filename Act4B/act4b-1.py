A = {'a', 'b', 'c', 'g', 'd', 'f'}
B = {'l', 'm', 'o', 'b', 'c', 'h'}
C = {'c', 'h', 'k', 'd', 'f', 'j', 'i'}

unionAB = A | B
print("Number of elements in set A and B:", len(unionAB))

bonly = B - (A | C)
print("Number of elements in B that is not part of A and C:", len(bonly))

print("Show the following using set operations:")
i = C - (A | B) | (B & C) - (A & B & C)
ii = A & C
iii = (A & B) | (B & C)
iv = (A & C) - B
v = A & B & C
vi = B - (A | C)

print("i.", i)
print("ii.", ii)
print("iii.", iii)
print("iv.", iv)
print("v.", v)
print("vi.", vi)
