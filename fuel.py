def main():
    inp = input("Enter Y/Z ")
    fuel(inp)

def fuel(inp):
    y,z = inp.split('/')
    try :
        y = int(y)
        z = int(z)
        result = (100/z) * y
    except ValueError :
        print('There was a value error')
    except ZeroDivisionError :
        print('Diviion by zero ')
    else :
        print(f"{result}%")
    

if __name__ == "__main__":
    main()