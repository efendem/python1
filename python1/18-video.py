#print('Yaqin dostlaringiz royxatini tuzamiz.')
#ismlar=[]
#n=1
#while True:
    #savol=f"{n} dostingizning ismini kiriting:"
    #ism=input(savol)
    #ismlar.append(ism)
    #takrorlash=input("Yana ism qo'shasizmi? (ha/yo'q)")
    #n+=1
    #if takrorlash!='ha':
        #break
#print("Do'stlaringiz yoshini saqlaymiz.")
#dostlar = {}
#ishora = True
#while ishora:
 #ism=input("Do'stingiz ismini kiriting. ")
 #yosh=input(f"{ism.title()}ning yoshini kiriting: ")
 #dostlar[ism] = int(yosh)

#javob=input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#if javob =="yo'q":
 #       ishora=False

#for ism, yosh in dostlar.items():
        #print(f"{ism.title()} {yosh} yoshda")
sonlar=[25, 63, 861, 25, 946, 25]
while 25 in sonlar:
    sonlar.remove(25)
    print(sonlar)