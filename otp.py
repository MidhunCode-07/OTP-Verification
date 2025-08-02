import random
a=random.randint(1000000,9999999)
print(a)

otp=int(input("Enter otp"))
if otp==a:
    print("verified successfully")
else:
    print("invalid")
