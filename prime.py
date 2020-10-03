def is_prime(n):
        if n < 2:
            return False
        prime = True
        for x in range(2, n):
            if n % x == 0:
                print(n, "is Divisible by", x)
                prime = False
                return prime
        return prime

while True:
    inputNum = int(input("Please input number: "))
    if inputNum == 0:
        break
    prime = is_prime(inputNum)
    if prime is True:
        print(inputNum," is a prime number")
    else:
        print(inputNum," is not a prime number")
        

# another method
num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       

else:
   print(num,"is not a prime number")

