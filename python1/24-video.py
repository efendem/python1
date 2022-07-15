#import math
#def daraja(n):
 #   return lambda x: x**n


#kvadrat = daraja(2)
#kub=daraja(3)
#print(f"3ning kvadrati {kvadrat(3)}ga, "
       # f"kubi {kub(3)} ga teng")
from math import sqrt
sonlar=list(range(11))
#ildizlar=list(map(sqrt,sonlar))
kvadratlar=list(map(lambda x:x*x,sonlar))
print(sonlar)
print(kvadratlar)