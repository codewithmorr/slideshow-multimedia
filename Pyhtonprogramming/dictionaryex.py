student = {
    "name": "karl",
    "age": 20,
    "course":"BBIT"

}

print(f"Name:{student['name']}, Age:{student['age']}")


#add and update

student["hobby"] = "Football"
student["age"] = 21
print(student)


#removing items

student.pop("hobby")
print(student)

#looping through a dictionary
for key,value in student.items():
    print(key, ":", value)

#bonus

capitals = {
    "kenya" : "nairobi",
    "Tanzania": "Dodoma",
    "Uganda":"Kampala"
}

#accessing values
print(capitals["Tanzania"])
