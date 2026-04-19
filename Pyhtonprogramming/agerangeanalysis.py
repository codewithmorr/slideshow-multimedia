print("welcome to age range analysis")

name = input("Enter your name:")
age = int(input("Enter your age:"))

current_year = 2025
birth_year = current_year - age

if 1997 <= birth_year<2010:
   generation = "Generation Z"
elif 2010 <= birth_year < 2025:
    generation = "Generation Alpha"
elif 1981<= birth_year < 1997:
    generation = "Millennials"
  
elif 1965 <= birth_year < 1981:
    generation = "Generation X"
   
elif 1946 <= birth_year < 1965:
    generation = "Baby Boomers"
    
elif birth_year < 1946:
   generation = "Silent Generation"
else:
    generation = "Unknown Generation"

print(f"Hello {name}, you were born in {birth_year}. You belong to the {generation}.")


if age < 18:
    print(f"this many till you can vote but for some reason you can drive{current_year + (18 - age)}")
elif age < 30:
    print(f"you still got a couple till your mom start asking for grandkids yet was too strict about you having a boyfriend or girlefriend{current_year + (30 - age)}")
elif age < 40:
    print(f"you are getting old but you still got a couple till you start getting back pain{current_year + (40 - age)}")
elif age < 50:
    print(f"you good but but man damn not long ago you were dying your hair white now you dying it black but we see the grays though{current_year + (50 - age)}")
elif age < 60:
    print(f"hi old peaple you should be looking at retirement abit more seriously icl{current_year + (60 - age)}")
elif age < 70:
    print(f"you are up there now{current_year + (70 - age)}")
elif age < 80:
    print(f"you are old now but you still got a couple till you start losing hearing{current_year + (80 - age)}")
elif age < 90:
    print(f"you are really old now but you still got a couple till you start hearing things {current_year + (90 - age)}")
elif age < 100:
    print(f"you are really really old now but you still got a couple till you start forgetting yourself but it is calm no pressure{current_year + (100 - age)}")
else:
    print(f"you are really really really old now but you still got a couple till you start forgetting your name but it is calm no pressure{current_year + (110 - age)}")


print("\n ------Summary------")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Birth Year: {birth_year}")
print(f"Generation: {generation}")
