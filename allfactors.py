def factorial(x):
    print("the factors of",x,"are:")
    for i in range(1,x+1):
        if x%i==0:
            print(i)
n=int(input("enter the number:"))
factorial(n)
