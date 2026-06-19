print("=== Student Profile Generator ===")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
dept = input("Enter your department: ")
marks = int(input("Enter your marks: "))

print("\n===== PROFILE =====")
print(f"Name       : {name}")
print(f"Age        : {age}")
print(f"Department : {dept}")
print(f"Marks      : {marks}")

if marks >= 40:
    print("Result     : PASS ✅")
else:
    print("Result     : FAIL ❌")
