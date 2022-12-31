# EX1

nums = [12,75,150,180,145,525,50]

for value in nums:
    if value % 5 == 0:
        if value <= 150:
            print(value)
            continue
        if value >= 500:
         break


print("Done!")


# Ex2

num=int(input("please enter a num"))
reversed_num=0

while num !=0:
    digit=num%10
    reversed_num = reversed_num * 10+digit
    num //= 10
print("Reversed Number: " + str(reversed_num))