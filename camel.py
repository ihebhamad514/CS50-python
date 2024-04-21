def main():
    inp = input("Camel case : ")
    snake = snakecase(inp)
    print(f"Snake case : {snake}")

def snakecase(inp):
    snake = ""
    for letter in inp :
        if letter.isupper():
            snake = snake + "_" + letter.lower()
        else : 
            snake = snake + letter
    return snake

if __name__ == "__main__":
    main()