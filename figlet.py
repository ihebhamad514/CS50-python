import sys
from pyfiglet import Figlet


def main():
    figlet()

def figlet():
    if len(sys.argv) == 3 :
        f = Figlet(font=sys.argv[2])
    elif len(sys.argv) == 1:
        f = Figlet()
    else :
        print("Usage python figlet.py -f/-font font")
    inp = input("Input: ")
    print (f.renderText(inp))

if __name__ == "__main__":
    main()
