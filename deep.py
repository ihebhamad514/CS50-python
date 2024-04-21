def main():
    print(deep())

def deep():
    inp = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    if inp in ["42", "forty two", "forty-two"] : 
        return "Yes"
    return "No"

if __name__ == "__main__":
    main()