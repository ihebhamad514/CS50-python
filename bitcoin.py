import requests
import sys

def main():
    try :
        n = float(sys.argv[1])
    except IndexError:
        sys.exit()
    except ValueError:
        sys.exit()

    n = float(sys.argv[1])
    get_json(n)
def get_json(n):
    response = requests.request("GET","https://api.coindesk.com/v1/bpi/currentprice.json")
    print(response.json()["bpi"]["USD"]["rate_float"]*n)

if __name__ == "__main__":
    main()