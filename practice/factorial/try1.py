
def factorial(number):
    if number == 0:
       return 1
    else:
        return number * factorial(number-1) 

def NumberOfZeroInFactorial(number):
    fac=factorial(number)
    count=0
    while (fac%10==0):
        count= count+1
        fac= fac/10
    return count



number=int(input("[+]please enter number : \n "))
fac = factorial(number)
print("[+] Result = {:20}" .format(fac))
print(NumberOfZeroInFactorial(number))
