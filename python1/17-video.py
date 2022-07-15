#son=1
#while son<=5:
    #print(son)
    #son=son+1

    #print('Dastur tugadi')

    #print('kiritlgan sonning kvadratini qaytaruvchi dastur.')
    #savol='istalgan sonni kiriting'
    #savol+= "dasturni to'xtatish uchun 'exit'ni kiriting: "
    #qiymat=''
    #while qiymat!='exit':
        #qiymat=input(savol)
        #if qiymat!='exit':
           # print(float(qiymat)**2)
sonlar=list(range(1,11))
for son in sonlar:
                if son==5:
                    continue
                print(f"{son}ning kvadrati{son**2}ga teng")