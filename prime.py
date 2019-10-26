def findPrimeRange(a,b):
    """
    DOCSTRING: This function is written to find all prime numbers between two given integers.(not including given numbers)
    If you'd like to change this situation I left a commend line in there.

    INPUT: You need to enter two integers for the parameters. 

    OUTPUT:This function is going to print all of prime numbers between those. 
    """
    if a<=0 or b<=1:
        print("Please enter a valid values for parameters.")
        return

    isPrime = False
    for i in range(a+1,b):#if you'd like to include the numbers sent, just use it instead --->range(a,b+1)
        for j in range(2,i):
            if i%j==0:
                isPrime=False
                break
            isPrime = True
        if isPrime or i==2:
            print(f"{i} is a prime number.")
findPrimeRange(1,20)