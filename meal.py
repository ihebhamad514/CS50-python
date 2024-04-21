def main():
    time = input("Time: ")
    time = convert(time)
    if  7.00 <= time <= 8.00 :
        print("breakfast meal")
    elif 12.00 <= time <= 13.00 :
        print("lunch meal")
    elif 18.00 <= time <= 19.00:
        print("dinner meal")


def convert(time):
    return float(time.replace(":","."))


if __name__ == "__main__":
    main()