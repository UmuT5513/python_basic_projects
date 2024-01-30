name = "abc"
passw = "12345"

user_name = input("Kullanıcı adını girin: ")
password = input("Parolanızı girin: ")

a = True

while a:
    if user_name == name and password == passw:
        print("Bilgileriniz doğru, Giriş başarılı!")
        a = False
    elif user_name == name and password != passw:
        print("Girilen parola yanlış!")
        a = False
    elif user_name != name and password == passw:
        print("Girilen kullanıcı adı yanlış!")
        a = False
    else:
        print("Girilen parola ve kullanıcı adınız yanlış!")
        a = False