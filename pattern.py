print("The half triangle of * ")
n=int(input("Enter how much line you want to be your halftriangl: "))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()