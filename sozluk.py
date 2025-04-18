list = {
        "CRINGE": "garip ya da utandırıcı bir şey",
        "LOL": "komik bir şeye verilen cevap",
        "ROFL": "bir şakaya karşılık cevap",
        "SHEESH": "onaylamamak",
        "CREEPY": "korkunç",
        "AGGRO": "agresifleşmek/sinirlenmek"
        }

word = input("anlamadığınız bir kelime yazın(hepsi büyük harf olmalı!):")

if word in list.keys():
   print (list[word])
else:
    print ("böyle bir kelime bilinmiyor")
