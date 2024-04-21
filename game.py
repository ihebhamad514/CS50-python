import random

def main():
    game()

def game():
    n = int(input("Level: "))
    guess = random.randint(1,n)
    while True:
        try :
            inp = int(input("Guess : "))
        except ValueError :
            pass
        else :
            if inp < guess :
                print("Too small !!")
            elif inp > guess :
                print("Too large !!")
            else : 
                print("Just right !!")
                break

if __name__ == "__main__":
    main()