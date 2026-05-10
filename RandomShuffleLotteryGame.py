import random

# Lottery Number Generator
# Usingrandom.sample() 

def generate_lottery_numbers():
    print("=====================================")
    print("Official Lottery Draw Now Happening!")
    print("=====================================")
    
    # Define The Range (1 to 50)
    # Range(1, 51) Includes Numbers From 1 To 50
    pool = range(1, 51)
    
    # random.sample(size, n)
    # This Picks 'n' Unique Elements From The Pool
    draw = random.sample(pool, 6)
    
    # Sort The Numbers From Lowest To Highest For The Ticket
    draw.sort()
    
    print(f"Tonight's Winning Numbers Are: {draw}")
    print("Good Luck Player !")

if __name__ == "__main__":
    generate_lottery_numbers()
