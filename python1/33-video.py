with open('pi.txt') as fayl:
    pi = fayl.read()
    fayl = open('pi.txt')
PI = fayl.read()
print(pi)
fayl.close()
pi = pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
pi = pi.replace('\n','') # qator tashlash belgisini almashtiramiz
pi = float(pi) # matnni float (o'nlik) songa o'tkazamiz
print(pi)
with open('data/pi.txt') as fayl:
    pi = fayl.read()
    faylnomi = 'data/math/numbers/pi.txt'
with open(faylnomi) as fayl:
    pi = fayl.read()
    filename = 'data/talabalar.txt'
with open(filename) as file:
    for line in file:
        print(line)