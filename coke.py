def main():
    coke()

def coke():
    balance = 50
    while balance != 0:
        print(f"Amount due {balance}")
        amount = int(input("Insert coin : "))
        if amount not in [5, 10, 25]:
            pass
        else : 
            balance -= amount

if __name__ == "__main__":
    main()