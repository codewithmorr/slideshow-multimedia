student = ("Karl", 20, "BBIT")
print(f"Name:{student[0]} Age:{student[1]}. Course:{student[2]}")
# tuple unpacking



#slicing tuples

nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(nums[0:3])#prints first 3 numbers
print(nums[5:])#prints numbers from index 5 to the end


#tuples in tuples

nested_tuple = (("Kenya", "Nairobi"), ("Tanzania", "Dodoma"))
print(nested_tuple[0][1])
# Output: Nairobi
print(nested_tuple[1][1])# Output: dodoma



footballers = ("Messi", "Ronaldo", "Neymar", "Mbappe")
print("The best footballers are:")
print(footballers[0])  # Output: Messi
print(footballers[1])  # Output: Ronaldo
print(footballers[2])  # Output: Neymar
