def summa(*sonlar):
    """Kiritilayotgan sonlar yig'indisini hisoblaydigan funksiya"""
    yigindi=0
    for son in sonlar:
        yigindi += son
    return yigindi
print(summa(1,2,3,4,5))
print(summa(4,6,7))

def summa(*sonlar):
    """Kiritilayotgan sonlar yig'indisini hisoblaydigan funksiya"""
    
    return sum(sonlar)
print(summa(1,2,3,4,5))
print(summa(4,6,7))
