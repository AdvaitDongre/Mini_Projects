#to code and a message and decode it
ques = input("Do you want to code or decode a message?\n")

if ques == "code":

    word = input("What is the word?\n")

    if (len(word) >= 3 ):

        import string
        import random

        
        code = random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + word[1:] +  word[0] + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)

        print(code)
        
    else:
        code = word[1:] + word[0]
        print(code)
        


elif ques == "decode":

    word = input("What is the word?\n") 

    code = word[-4] + word[3:-4]
    print(code)
    
    

else:
    print("Sorry your input is wrong\n")


    
print("made by Advait")