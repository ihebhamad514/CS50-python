def main():
    gorcery()

def gorcery():
    menu = {}
    while True :
        try :
            inp = input("")
            try:
                menu[inp] = menu[inp]+1  
            except KeyError:
                menu[inp] = 1
        except EOFError:
            print("")
            for _ in menu :
                print(_," " ,menu[_])
            break



if __name__ == "__main__":
    main()