# a quiz game 
# 1 to make the questions 
# 2 to keep track of the scores
# 3 take the answer
import time
print("Welcome to the better KBC\n made by Advait\n")
time.sleep(2)
print("I hope you score good, lets start\n")
time.sleep(2)
class game:
    def questions(ques, a, b, c, d):
        print(ques)
        time.sleep(2)
        print(f"a){a}\n b) {b}\n c){c}\n d){d}\n")
        time.sleep(1)
        print("What is your answer?\n")

tries = 0
def idk(a):
    if a != "a" and a != "b" and a != "c"and a != "d":
        print("Sorry Invalid input try again")
        return

q1 = game 
q1.questions("What is the capital of India?", "Delhi", "Maharastra", "Chennai", "Tamil Nadu")
a = input()
idk(a)
if a == "a":
    tries = tries + 1

q2 = game
q2.questions("What is my name?", "Adi", "Advait", "Aashu", "Idk")
a = input()
idk(a)
if a == "b":
    tries = tries +1

# this is the ideal template and you can add more questions

print(f"This is the points you have: {tries}")  

        



        

    

