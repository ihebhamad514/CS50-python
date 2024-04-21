def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    pos_c = -1 
    pos_n = -1
    for _ in s :
        if not _.isalpha() and not _.isnumeric():
            return False
        elif _.isnumeric() :
            pos_n = s.index(_)
        elif _.isalpha() and pos_n != -1:
            pos_c = s.index(_)
        if pos_c > pos_n :
            return False
           

    if 2 <= len(s) <= 6 and s[0:2].isalpha() : 
        return True
    return False

if __name__ == "__main__":
    main()
