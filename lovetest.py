import random
def lovetest():
    print("Welcome To The Love Test App")
    print("Please Enter The Boy's Name: ")
    a=str(input())
    a=a.title()
    print("Please Enter The Girl's Name :")
    b=str(input())
    b=b.title()
    A=[100,99,98,97,96,95,94,93,92,90,89,88,87,86,85,83,84,82,81,80,79,78,77,76,75,74,73,72,71,70]
    B=[0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30]
    C=random.choice(A)
    D=random.choice(B)
    print("Love is an intense feeling or affection to someone")
    print("Lets see how much love you have.............")
    print(a,"loves ",b," ",C,"%")
    print(b," loves ",a," ",D,"%")
    print(a,", My dear user I think you should test your face first!!!!")
    print("But dont be sad we love you.....")

lovetest()
print("Do You Want To Try Again??? Then Press 1")
e=int(input())
if (e==1):
    lovetest()
else:
    exit()
