from googletrans import Translator
tarjimon = Translator() 
matn_uz = "Python - dunyodagi eng mashxur dasturlash tili"
tarjima = tarjimon.translate(matn_uz)
print(tarjima.text)
tarjima_ru = tarjimon.translate(matn_uz, dest='ru')
print(tarjima_ru.text)
tarjima_uz = tarjimon.translate(matn_en, src='uz', dest='uz')
