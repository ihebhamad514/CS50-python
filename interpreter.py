def main():
    inp = input("Calculate : ")
    x, y, z = inp.split(" ")
    print(interpreter(x,y,z))

def interpreter(x,y,z):
    match y :
        case "+":
            return int(x) + int(z)
        case "-":
            return int(x) - int(z)
        case "*":
            return int(x) * int(z)
        case "/":
            return int(x) / int(z)
        case _ :
            return "No operation is provided"

if __name__ == "__main__":
    main()