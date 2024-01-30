from random import randint

def check_answer(guess, random):
    if guess > random:
        print("Daha küçük bir sayı tahmin et!")
    elif guess < random:
        print("Daha büyük bir sayı tahmin et!")
    else:
        print("Doğru tahmin!")

def game():
    random_num = randint(1, 100)
    print(random_num)
    user_num = 0
    while user_num != random_num:
        user_num = int(input("Enter a number between 1 and 100: "))
        check_answer(user_num, random_num)

game()










 # Yaptığım hata
#def game():
#    random_num = randint(1, 100)
#    print(random_num)
#    user_num = int(input("Enter a number between 1 and 100: "))
#
#    while user_num != random_num:
#        check_answer(user_num, random_num)
#        user_num = int(input("Enter a number between 1 and 100: "))