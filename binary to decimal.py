#wap a program binary to decimal.
n=int(input("Enter the binary digit:"))
s=0
for y in range n:
    for x in range(0,n-1):  
        r=n%10
        s=s+r*2**n
        n=n//10
        print(s)
input()
