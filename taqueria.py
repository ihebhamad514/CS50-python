def main():
    taqueria()

def taqueria():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

    total = 0    
    while True :
        try:
            inp = input("Food: ")
        except EOFError :
            break
           
        if inp in menu:
           total+=menu[inp]
        print(f"Total : {total}")

if __name__ == "__main__":
    main()