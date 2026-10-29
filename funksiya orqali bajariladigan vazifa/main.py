def dasturni_bajar():
    # 1. Davlatlar ro'yxatini tuzish va chiqarish
    davlatlar = ["O'zbekiston", "Turkiya", "AQSh", "Yaponiya", "Germaniya"]
    print("--- 1-7. DAVLATLAR RO'YXATI ---")
    print("Asl ro'yxat:", davlatlar)

    # 2. Ro'yxatning uzunligini chiqarish
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

    # 8. 120 dan 1200 gacha bo'lgan juft sonlar ro'yxati
    juft_sonlar = list(range(120, 1201, 2))

    print("\n--- 8-12. JUFT SONLAR BILAN ISHLASH ---")
    # 9. Sonlar yig'indisini hisoblash (for tsikli yordamida)
    yigindi = 0
    for son in juft_sonlar:
        yigindi = yigindi + son
    print("Sonlar yig'indisi:", yigindi)

    # 10. Eng katta va eng kichik son orasidagi ayirma
    eng_kichik = 120
    eng_katta = 1200
    ayirma = eng_katta - eng_kichik
    print("Eng katta va eng kichik son ayirmasi:", ayirma)

    # 11. Elementlar sonini hisoblash (tsikl yordamida)
    elementlar_soni = 0
    for element in juft_sonlar:
        elementlar_soni = elementlar_soni + 1
    print("Elementlar soni:", elementlar_soni)

    # 12. Boshidan, o'rtasidan va oxiridan 20 ta qiymatni chiqarish
    print("Boshidan 20 ta:")
    for i in range(20):
        print(juft_sonlar[i], end=" ")
    print()

    orta_indeks = elementlar_soni // 2
    print("O'rtasidan 20 ta:")
    for i in range(orta_indeks - 10, orta_indeks + 10):
        print(juft_sonlar[i], end=" ")
    print()

    print("Oxiridan 20 ta:")
    for i in range(elementlar_soni - 20, elementlar_soni):
        print(juft_sonlar[i], end=" ")
    print()

    # 13-15. Taomlar va nonushta ro'yxati
    print("\n--- 13-15. TAOMLAR VA NONUSHTA ---")
    taomlar = ["Osh", "Shashlik", "Manti", "Somsa", "Lag'mon"]
    nonushta = list(taomlar)
    nonushta.remove("Osh")
    nonushta.remove("Shashlik")
    nonushta.append("Tuxum")
    nonushta.append("Choy")
    
    print("Asl taomlar ro'yxati:", taomlar)
    print("Nonushta ro'yxati:", nonushta)

# Funksiyani ishga tushirish
dasturni_bajar()
