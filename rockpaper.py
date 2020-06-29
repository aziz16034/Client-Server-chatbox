import random

#Rock, Paper, Scissor project by Abdul Aziz, 6/8/2020
def playgame():

 print("The Rules of Rock paper scissor game will be follows: \n"
+"Rock vs paper --> paper wins \n"
+"Rock vs scissor --> Rock wins \n"
+"paper vs scissor --> scissor wins \n")


 print("Now please enter your choice no. \n 1. Rock \n 2. paper \n 3. scissor \n")
 user = int(input("Now Your turn: "))

 abcd = random.randint(1,3)

 if abcd ==1:
    print("Computer has rock")

 elif abcd ==2:
    print("Computer has paper")

 elif abcd ==3:
    print("Computer has scissor")

 while user> 3 or user< 1:
   user = int(input("Enter your valid input here: "))



 while user == 1 or 2 or 3:

    if user == abcd:

        print("tie")
        break

    elif int( abcd == 3 and user == 1):
        print("You win")
        break

    elif int(abcd == 2 and user == 1 ):
        print("computer wins")
        break

    elif int(abcd == 1 and user == 2 ):
        print("you win")
        break

    elif int(abcd == 3 and user == 2 ):
        print("computer wins")
        break

    elif int(abcd == 1 and user == 3 ):
        print("computer wins")
        break

    elif int(abcd == 2 and user == 3 ):
        print("you win")

        break


def playagain():
 again = str(input("Type Q for quit or press another key to play again"))

 while again == "Q":
      print("Thank you for playing")
      break

 while again != 'Q':

     playgame()
     playagain()



class main():
 playgame()
 playagain()

