import random

print(("-" * 30) + "\nTaş, Kağıt, Makas\n" + ("-" * 30))

user_score, computer_score = 0, 0

while True:
    print("\n1 - Taş\n2 - Kağıt\n3 - Makas")
    user_choice = input("Seçimin: ")
    computer_choice = random.choice(["1", "2", "3"])
    
    if user_choice == "1":
        if computer_choice == "1":
            print("Bilgisayarın seçimi: Taş\nTaşa taş. Beraberlik!")
            
        elif computer_choice == "2":
            print("Bilgisyaraın seçimi: Kağıt\nKağıt taşı sarar. Kaybettiniz!")
            computer_score += 100
            
        elif computer_choice == "3":
            print("Bilgisayarın seçimi: Makas\nTaş makası kırar. Kazandınız!")
            user_score += 100
            
    elif user_choice == "2":
        if computer_choice == "1":
            print("Bilgisayarın seçimi: Taş\nKağıt taşı sarar. Kazandınız!")
            user_score += 100
            
        elif computer_choice == "2":
            print("Bilgisayarın seçimi: Kağıt\nKağıta kağıt. Beraberlik!")
            
        elif computer_choice == "3":
            print("Bilgisayarın seçimi: Makas\nMakas kağıdı keser. Kaybettiniz!")
            computer_score += 100
            
    elif user_choice == "3":
        if computer_choice == "1":
            print("Bilgisayarın seçimi: Taş\nTaş makası kırar. Kaybettiniz!")
            computer_score += 100
            
        elif computer_choice == "2":
            print("Bilgisayarın seçimi: Kağıt\nMakas kağıdı keser. Kazandınız!")
            user_score += 100
            
        elif computer_choice == "3":
            print("Bilgisayarın seçimi: Makas\nMakasa makas. Beraberlik!")
    
    else:
        break
    
print("\nOyuncu Skoru: {}\nBilgisayarın Skoru: {}".format(user_score, computer_score))