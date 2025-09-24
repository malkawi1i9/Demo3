def fizzbuzz(n1):
    if int(n1) % 3 == 0 and int(n1) % 5 == 0:
        return("FizzBuzz")
    elif int(n1) % 3 == 0:
        return("Fizz")
    elif int(n1) % 5 == 0:
        return("Buzz")
    else: 
        return(n1)

def main():
    n1 = input("enter your number: ")
    if n.isdigit():
        print(fizzbuzz(n1))
    else:
        print("invalid input")
        
if __name__ == "__main__":
    main()
