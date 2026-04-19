name = input("Enter your name: ")
age = int(input("Enter your age: "))
birth= 2025 - age
print(f"Hello {name}, you were born in {birth}.")
to100 = 100 - age

if age >100:
    print(f"{2025 + to100}. damn you aleady over 100 ")
else:
    print(f"You are not over 100 yet, you will be in {2025 + to100}.")