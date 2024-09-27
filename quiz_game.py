print("Welcome to my Quiz!")

s = 0
play= input("Do you want to play? ")
if play.lower() != "yes" :
    quit()
print("Okay, Let's Play")

q1= input("What does CPU stands for? ").lower()
if q1 == "Cental Processing Unit":
    print("Correct")
    s +=1
else:
    print("Incorrect!")
q2= input("What does GPU stand for? ").lower()
if q2 == "Graphics Processing Unit":
    print("Correct")
    s +=1
else:
    print("Incorrect!")
q3= input("What does RAM stand for? ").lower()
if q3 == "Random Access Memory":
    print("Correct")
    s +=1
else:
    print("Incorrect!")
q4= input("What does USB stand for? ").lower()
if q4 == "Universal Serial Bus":
    print("Correct")
    s +=1
else:
    print("Incorrect!")
q5= input("What is a virus? ").lower()
if q5 == "Malicious software":
    print("Correct")
    s +=1
else:
    print("Incorrect!")

print(f"Your percentage is  " + {s*20} )
