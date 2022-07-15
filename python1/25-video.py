import random

def sontop(x=10):
    tasodifiy_son=random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?")
    taxminlar=0
    while True:
        taxminlar += 1
        taxmin=int(input(">>>"))
        if taxmin<tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling:")
        elif taxmin>tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling:")
        else:
            break
        return taxminlar
    print(f"Tabriklaymiz! {taxminlar} taxmin bilan topdingiz!")
def sontop_pc(x=10):
    input(f"1dan {x}gacha istalgan son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi=1
    yuqori=x
    while True:
        if quyi != yuqori:
            taxmin=random.randint(quyi, yuqori)
        else:
            taxmin= quyi
        javob=input(f"Siz{taxmin} sonni o'yladingiz: to'g'ri(t),"
        f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob =="-":
                yuqori= taxmin-1
        elif javob=="+":
                quyi=taxmin+1
        else:
             break
        print("Topdim!")
