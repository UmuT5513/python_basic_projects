import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

elements = [rock, paper, scissors]

computer = random.randint(0, 2)
user_choice = int(input("Hangisini seçmek istiyorsun! Taş için 0, Kağıt için 1, Makas için 2 girin: "))

print(f"Bilgisayarın seçimi: {elements[computer]}")
print(f"Senin seçimin: {elements[user_choice]}")

if user_choice >= 3 or user_choice < 0:
    print("Lütfen geçerli aralıkta bir sayı girin!")
else:
    print("Lütfen geçerli aralıkta bir sayı girin!")



if user_choice == 0 and computer == 2:
    print("Kazandın!")
elif user_choice == 0 and computer == 1:
    print("Kaybettin!")
elif user_choice == 1 and computer == 2:
    print("Kaybettin")
elif user_choice == 1 and computer == 0:
    print("Kazandın")
elif user_choice == 2 and computer == 0:
    print("Kaybettin")
elif user_choice == 2 and computer == 0:
    print("Kaybettin")
else:
    print("Berabere!")


