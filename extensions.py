def main():
    ext = input("File name: ")
    ext = ext.split(".")[1]
    print(extensions(ext))

def extensions(ext):
    match ext :
        case "doc" :
            return "application/msword"
        case "jpg":
            return "jpeg"
        case "txt" : 
            return "text"
        case _ : 
            return "Extension is not found"

if __name__ == "__main__" : 
    main()