n=int(input("Enter number of rows: "))
number=1
print("floyd triangle")
for i in range(1,n+1):
    for y in range(1,i+1):
        print(number,end="")
        number=number+1
    print()