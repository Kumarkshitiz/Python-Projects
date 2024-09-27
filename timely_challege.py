import random
import time

OPERATORS = ["+","-","*"]
MIN_OPERATOR = 3
MAX_OPERATOR = 12
TOTAL_PROBLEMS = 5 

def generate_problem():
    left = random.randint(MIN_OPERATOR,MAX_OPERATOR)
    rigt = random.randint(MIN_OPERATOR,MAX_OPERATOR)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(rigt)  
    answer = eval(expr)
    return expr , answer

wrong = 0 
input("Press Enter to Start ")
print("--------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input(f"Problem no. str{i+1}  : {expr}   " )
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()

print("--------------")
print(f"You finished the challege in  {round(end_time-start_time ,2)} ")
print("Nice Work ")