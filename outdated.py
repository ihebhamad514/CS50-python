def main():
    outdated()

def outdated():
    _r = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    try :
        inp = input("Date: ")
    except :
        print ("error")
    fst = inp.split("/")
    if len(fst) == 3 :
        y = int(fst[2])
        d = int(fst[1])
        m = int(fst[0])
        print(f"{y}-{d:02}-{m:02}")
    else:
        inp = inp.split(" ")
        y = int(inp[2])
        d = int(inp[1].replace(",",""))
        m = int(_r.index(inp[0]))
        print(f"{y}-{d:02}-{m:02}")


if __name__ == "__main__":
    main()
