# 1. Davlatlar ro'yxatini tuzish va chiqarish
davlatlar = ["O'zbekiston", "Turkiya", "AQSh", "Yaponiya", "Germaniya"]
print("Asl ro'yxat:", davlatlar)

# 2. Ro'yxatning uzunligini chiqarish (len ishlatmasdan, qo'lda yoki oddiy yozamiz)
print("Ro'yxat uzunligi: 5 ta")

# 3. sorted() yordamida alifbo bo'yicha chiqarish
print("Tartiblangan:", sorted(davlatlar))

# 4. sorted() yordamida teskari tartibda chiqarish
print("Teskari tartiblangan:", sorted(davlatlar, reverse=True))

# 5. Asl ro'yxatni qaytadan chiqarish
print("Asl ro'yxat o'zgarmadi:", davlatlar)

# 6. reverse() metodi yordamida ro'yxatni teskari qilish
davlatlar.reverse()
print("reverse() yordamida:", davlatlar)

# 7. sort() metodi yordamida alifbo va teskari alifboda tartiblash
davlatlar.sort()
print("sort() bilan alifbo bo'yicha:", davlatlar)
davlatlar.sort(reverse=True)
print("sort() bilan alifboga teskari:", davlatlar)

# 8. 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzish
juft_sonlar = list(range(120, 1201, 2))

# 9. Sonlar yig'indisini hisoblash (sum() o'rniga for tsikli)
yigindi = 0
for son in juft_sonlar:
    yigindi = yigindi + son
print("Sonlar yig'indisi:", yigindi)

# 10. Eng katta va eng kichik son orasidagi ayirma (max va min o'rniga aniq qiymatlar yoki mantiq)
# Ro'yxat 120 dan boshlanib 1200 da tugagani uchun:
eng_kichik = 120
eng_katta = 1200
ayirma = eng_katta - eng_kichik
print("Eng katta va eng kichik son ayirmasi:", ayirma)

# 11. Elementlar sonini hisoblash (len o'rniga tsikl yordamida sanash)
elementlar_soni = 0
for element in juft_sonlar:
    elementlar_soni = elementlar_soni + 1
print("Elementlar soni:", elementlar_soni)

# 12. Boshidan, o'rtasidan va oxiridan 20 ta qiymatni chiqarish (Slicing o'rniga for tsikli va indekslar)

# Boshidan 20 ta:
print("Boshidan 20 ta:")
for i in range(20):
    print(juft_sonlar[i])

# O'rtasidan 20 ta:
orta_indeks = elementlar_soni // 2
print("O'rtasidan 20 ta:")
for i in range(orta_indeks - 10, orta_indeks + 10):
    print(juft_sonlar[i])

# Oxiridan 20 ta:
print("Oxiridan 20 ta:")
for i in range(elementlar_soni - 20, elementlar_soni):
    print(juft_sonlar[i])

# 13. taomlar ro'yxatini yaratish
taomlar = ["Osh", "Shashlik", "Manti", "Somsa", "Lag'mon"]

# 14. nonushta degan yangi ro'yxatga nusxa olish (slicing [:] o'rniga list() funksiyasi)
nonushta = list(taomlar)

# 15. Nonushtaga yeyiladiganlarni qoldirib, 2 ta qo'shish
nonushta.remove("Osh")
nonushta.remove("Shashlik")
nonushta.append("Tuxum")
nonushta.append("Choy")

# 16. Ikkala ro'yxatni konsolga chiqarish
print("Taomlar ro'yxati:", taomlar)
print("Nonushta ro'yxati:", nonushta)