m1 = int(input("Enter Mark 1: "))
m2 = int(input("Enter Mark 2: "))
m3 = int(input("Enter Mark 3: "))

total = m1 + m2 + m3
average = total / 3

print("Total Marks:", total)
print("Average:", average)

if average >= 50:
    print("Pass")
else:
    print("Fail")
