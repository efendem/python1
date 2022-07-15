#def toliq_ism_yasa(ism, familiya):
   # """Toliq ism qaytaruvchi funksiya"""
  #  toliq_ism=f"{ism} {familiya}"
 #   return toliq_ism

#talaba=toliq_ism_yasa("olim", "hakimov")
def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
    avto={'kompaniya':kompaniya,
    'model':model,
    'rang':rangi,
    'korobka':korobka,
    'yil':yili,
    'narx':narxi}
    return avto
avto1=avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2018)
avto2=avto_info('GM', 'Gentra', 'Oq', 'Mexanika', 2016, 15000)
avtolar=[avto1, avto2]
print("Online bozordagi mavjud avtomashinalar:")
for avto in avtolar:
     narx=avto['narx']
else:
     narx="Noma'lum"
print(f"{avto['rang']} {avto['model']}. Narxi:{narx}")
def oraliq(min,max):
    sonlar=[]
    while min<max:
        sonlar.append(min)
        min+=1
        return sonlar
print(oraliq(0,10))
print(oraliq(10,21))
