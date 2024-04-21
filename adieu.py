import inflect

def main():
    adieu()

def adieu():
    p = inflect.engine()
    _arr = []    
    while True :
        try : 
            inp = input("")
            _arr.append(inp)
        except EOFError :
            break
    print("Adieu, adieu, to",p.join(_arr))
    
if __name__ == "__main__":
    main()
