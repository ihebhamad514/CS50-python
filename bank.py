def main():
    inp = input("Greeting : ")
    print(bank(inp))

def bank(inp):
    if inp.lower().startswith("hello"):
        return "0$"
    elif inp.lower().startswith("h"):
        return "20$"
    else :
        return "100$"

if __name__ == "__main__":
    main()