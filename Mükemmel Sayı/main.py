
i = 1
sayi = int(input("Kontrol etmek istediğiniz sayiyi girin: "))
result = 0
while True:
    while i <= sayi / 2:
        if sayi % i == 0:
            result += i
            i += 1
        else:
            i += 1
    if result == sayi:
        print(f"{sayi} bir mükemmel sayidir!")
    else:
        print(f"{sayi} bir mükemmel sayi değildir!")
    break
