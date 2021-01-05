n=int(input("Enter the number : "))
d=2
tot=1
while n>1:
    if n%d==0:
        print(d)
        n/=d
        tot=tot*d
        continue
    d+=1
print("LCM is ",tot)
