def main():
    inp = input("Text : ")
    print(twttr(inp))

def twttr(inp):
    twttr_word = ""
    for _ in inp :
        if _.lower() not in "aeiou":
            twttr_word += _
    return twttr_word

if __name__ == "__main__":
    main()