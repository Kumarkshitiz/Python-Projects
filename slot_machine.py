import random


MAX_LINES = 3
MAX_BETS = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines



def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(coloumns):
    for row in range(len(coloumns[0])):
        for i, coloumn in enumerate (coloumns):
            if i != len(coloumns) - 1:
                print(coloumn[row]  , end= " | ")
            else:
                print(coloumn[row] , end= " ")
        print()     

def deposit():
    while True:
        amount = input("What is your Deposit amount ? ")
        if (amount.isdigit()):
            amount = int(amount)
            if amount > 0 :
                break
            else :
                print("Amount should be greater than Zero")
        else :
            print("Please Enter a number! ")
    
    return amount  

def get_no_of_lines():
    while True:
        lines = input("Enter the number of Lines  ")
        if (lines.isdigit()):
            lines  = int(lines)
            if 1 <= lines <= MAX_LINES :
                break
            else :
                print("Enter a valid no of Lines ")
        else :
            print("Please Enter a number! ")
    
    return lines  

def get_bets():
    while True:
        amount = input("What would you like to bet on each line? ")
        if (amount.isdigit()):
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BETS :
                break
            else :
                print("Amount should be Valid ")
        else :
            print("Please Enter a number! ")
    
    return amount  

def spin(balance):
    lines  = get_no_of_lines()
    while True:
        bet =  get_bets()
        total_bet = bet * lines
        if total_bet > balance :
            print(f"You don't have enough Balance to place the bet. Your current Balance is {balance} ")
        else :
            break

    print(f"You are betting {bet} on {lines} lines. Total bet is equal to {total_bet} ")

    slots = get_slot_machine_spin(ROWS , COLS , symbol_count)
    print_slot_machine(slots)
    winnigs, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnigs} ")
    print(f"You Won on lines  ", *winning_lines )

    return winnigs - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current Balance is {balance}")
        answer = input("Press Enter to Spin./ 'q' to quit  ")
        if answer == 'q':
            break
        balance += spin(balance)
    
    print(f"You are left with {balance} ")


if __name__ == "__main__" :
    main()