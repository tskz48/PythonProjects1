
import random
choice1=input("Choose rock, paper or scissors.")
choice1=choice1.lower()
s= {'rock','paper','scissors'}
choice2=random.choice(list(s))
print("Player's choice: "+str(choice1))
print("Computer's choice: "+str(choice2))


if choice1 == 'rock' and choice2 !='rock' :
    print("Player 1 wins") if choice2 =='scissors' else print("Player 2 wins.")

elif choice1 =='paper' and choice2!='paper':
    print("Player 1 wins") if choice2 =='rock' else print("Player 2 wins")
elif choice1 =='scissors' and choice2!='scissors' :
    print("Player 1 wins") if choice2=='paper' else print("Player 2 wins")

else:
    print("Game is a draw.")