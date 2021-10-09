import random


def win(user,computer):   #this funtion will check the winning results based on given conditons
  if (user=="s") and (computer=="p") or user=="p" and computer=="r" or user=="r" and computer=="s":
    return True


print("What's your choice??")
user=input("r for rock, s for scissors, p for paper: ")
computer=random.choice(['r','s','p'])  #r is for rock, s is for sissors, p is for paper.

if user== computer:  
  print("It's a draw")
  
if win(user,computer):
  print(f"Congratulations you won!! ,computer chooses {computer}")
else:
  print(f"Better luck next time, computer chooses {computer}")