import random
# adj = input("adjectives:")
# Verb1= input("Verb:")
# Verb2= input("Verb:")
# famous_person= input(" Famous Person: ")
# madlib =f"Computer programming is so {adj}! it makes so excited all the time because \
# I Love {Verb1}. Stay hydrated and{Verb2} Like you are {famous_person}"
 
# print(madlib)
def Guess(x):
      random_Number = random.randint(1,x)
      gues=0

      while gues != random_Number:
          gues=int(input(f"Guess a number between 1 and {x} \n"))
          if gues< random_Number:
              print("Sorry, Guess again.Too low number")
          elif gues> random_Number:
              print("Sorry,Guess again. To high ")       
      
      print(f"Congrats :You guess it right {random_Number} correct")


Guess(19)
