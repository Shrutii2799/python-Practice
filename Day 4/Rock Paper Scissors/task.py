import random

my_choice=int(input('what do you choose? Type 0 for rock ,1 for paper, 2 for scisssor?'))
#my_choice=random.randint(0,2)
#print("my choice")
print(my_choice)

if my_choice==0:
    print("""
    ___
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif my_choice==1:
    print("""
     ___
---'    __)__
           ______)
          _______)
         _______)
---.__________)
""")
else:
    print("""
    ___
---'   __)__
          ______)
       __________)
      (____)
---.__(___)
""")

print("computer choice")

computer_choice=["""
    ___
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""","""
     ___
---'    __)__
           ______)
          _______)
         _______)
---.__________)
""","""
    ___
---'   __)__
          ______)
       __________)
      (____)
---.__(___)
"""]

comp=random.randint(0,2)
print(computer_choice[comp])

if my_choice not in [0,1,2]:
    print("invalid input")
elif my_choice==0 and comp==1 :
    print(" computer won")

elif my_choice==0 and comp==2:
    print(" you won")

elif my_choice==1 and comp==0:
    print("you won")

elif my_choice==1 and comp==2 :
    print(" computer won")

elif my_choice==2 and comp==0 :
    print(" computer won")

elif my_choice==2 and comp==1 :
    print(" you won")
elif my_choice==0 and comp==0 :
    print(" tie")
elif my_choice==1 and comp==1 :
    print(" tie")
elif my_choice==2 and comp==2 :
    print(" tie")