def openFile(file_path):
    f=open(file_path)
    return f.readlines()
def in_line(lines):
    currencyDict = {}
    for line in lines:
	    parsed = line.split("\t")
	    currencyDict[parsed[0]] = parsed[1]
    return currencyDict
def show(lines, currencyDict):
    amount=float(input("enter ammout: \n"))
    print("enter currency name in which you want to convert from above list" )
    [print(item) for item in currencyDict.keys()]
    currency = input("Please enter one of these values: \n")
    print(f"{amount} INR is equal to {amount *float(currencyDict[currency])} {currency}")

if __name__ == "__main__":
    file_path="exchange.txt"
    lines= openFile(file_path)
    currencyDict= in_line(lines)
    show(lines, currencyDict)