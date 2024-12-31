def hmakinesi(secim):
    if secim == 1:
        s1 = int(input("Toplamak istediğiniz 1. sayıyı girin: "))
        s2 = int(input("Toplamak istediğiniz 2. sayıyı girin: "))
        return s1 + s2  # Toplama işleminin sonucunu döndürür
    elif secim == 2:
        s1 = int(input("Çıkarmak istediğiniz 1. sayıyı girin: "))
        s2 = int(input("Çıkarmak istediğiniz 2. sayıyı girin: "))
        return s1 - s2  # Çıkarma işleminin sonucunu döndürür
    elif secim == 3:
        s1 = int(input("Çarpmak istediğiniz 1. sayıyı girin: "))
        s2 = int(input("Çarpmak istediğiniz 2. sayıyı girin: "))
        return s1 * s2  # Çarpma işleminin sonucunu döndürür
    elif secim == 4:
        s1 = int(input("Bölmek istediğiniz 1. sayıyı girin: "))
        s2 = int(input("Bölmek istediğiniz 2. sayıyı girin: "))
        if s2 != 0:
            return s1 / s2  # Bölme işleminin sonucunu döndürür
        else:
            print("Hata: Bölme sıfıra yapılamaz!")
            return None  # Bölme sıfıra yapılmazsa None döndürülür
    else:
        print("Hatalı işlem girdiniz.")
        return None  # Geçersiz bir seçim yapılırsa None döndürülür

while True:
    print("Hangi işlemi yapmak istersin?")
    print("1. Toplama\n2. Çıkarma\n3. Çarpma\n4. Bölme")
    secim = int(input("İşlemi girin: "))

    # İşlemi yapıp sonucu 'result' değişkenine atıyoruz
    result = hmakinesi(secim)

    # Sonuç varsa ekrana yazdırıyoruz
    if result is not None:
        print(f"Sonuç: {result}")

    # Devam etmek için kontrol sorusu
    kontrol = input("Devam etmek için 'e' tuşuna basın, çıkmak için herhangi bir tuşa basın... ")
    if kontrol.lower() != 'e':
        print("Programdan çıkış yapıldı.")
        break
