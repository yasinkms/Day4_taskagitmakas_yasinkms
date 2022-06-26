import random
taş = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

kağıt = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

makas = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

da_poet=int(input("Hangisini seçeceksin? taş için 0, kağıt için 1, makas için 2 yazın.\n"))
if da_poet==0:
  print(taş)
elif da_poet==1:
  print(kağıt)
elif da_poet==2:
  print(makas)
else:
  print("Oyuna yeniden başlamalısın.")

print("Bilgisayar Seçimi")
a=[taş, kağıt, makas]
oyuncu_liste=random.randint(0,2)
print(a[oyuncu_liste])

if da_poet==0 and oyuncu_liste==0:
  print("berabere, yeniden dene")
elif da_poet==0 and oyuncu_liste==1:
  print("Kaybettin. Kağıt taşı yener.")
elif da_poet==0 and oyuncu_liste==2:
  print("Kazandın! Taş makası yener.")
elif da_poet==1 and oyuncu_liste==0:
  print("Kazandın! Kağıt taşı yener.")
elif da_poet==1 and oyuncu_liste==1:
  print("berabere, yeniden dene")
elif da_poet==1 and oyuncu_liste==2:
  print("Kaybettin. Makas kağıdı yener.")
elif da_poet==2 and oyuncu_liste==0:
  print("Kaybettin. Taş makası yener.")
elif da_poet==2 and oyuncu_liste==1:
  print("Kazandın! Makas kağıdı yener.")
elif da_poet==2 and oyuncu_liste==2:
  print("berabere, yeniden dene")  
