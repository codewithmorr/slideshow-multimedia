#creating a dictionary
student = {
    "name":"Karl",
    "age":20,
    "course":"BBIT"
}

#accessing dictionary values
print(f"Name:{student['name']}, Age:{student['age']}, Course:{student['course']}")


#adding and updating
student["age"] = 21 # update age
student["sports"] = "Basketball" #add a new key valuepair
print(student)



#removing\deleting a key-value pair
student.pop("sports") #remove sports
print(student)

#looping throuhg a dictionary
for key, value in student.items():
    print(key, ":", value)