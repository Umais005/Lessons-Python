# Lesson 8

dog = {}

dog["name"] = "Rex"
dog["colour"] = "brown"
dog["breed"] = "German Shepherd"
dog["legs"] = 4
dog["age"] = 5
print(dog)

student = {
    "first_name": "Muhammad",
    "last_name": "Umais",
    "gender": "Male",
    "age": 21,
    "marital_status": "Single",
    "skills": ["Python", "JavaScript", "HTML", "CSS"],
    "country": "Pakistan",
    "city": "Islamabad",
    "Address": "G-10/4"
}

print(len(student))

print(student["skills"])
print(type(student["skills"]))

student["skills"].extend(["C++", "Java"])

print(student.keys())
print(student.values())
print(student.items())

student.pop("marital_status")
print(student)
del dog
