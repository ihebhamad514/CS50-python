def main():
    faces()

def faces():
    inp = input("")
    inp = inp.replace(":)", "🙂")
    inp = inp.replace(":(", "🙁")  
    print(inp)  

if __name__ == "__main__":
    main()