a = "Thirty"
b = "Days"
c = "Of"
d = "Python"
f_string = f"{a} {b} {c} {d}"
print(f_string)

company = "Coding For All"

print(company)

print(len(company))

print(company.upper())

print(company.lower())

print(company.capitalize())

print(company.title())

print(company.swapcase())

cut = company[0:6]
print(cut)

print(company.index("Coding"))

print(company.split(" "))

sm = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(sm.split(","))

print(company[0])

print(company[-1])

print(company[0], company[7], company[11])

print(company.index("C"))

print(company.rindex("l"))

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))

print(sentence.rindex("because"))

print(sentence.replace("because", ""))

print(company.startswith("Coding"))
print(company.endswith("Company"))

new = "  Coding For All   "
print(new.strip())

radius = 10
area = 3.14 * radius ** 2

print(
    f"The area of a circle with radius {str(radius)} is {str(area)} meters squared.")

a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a}//{b}={a//b}")
print(f"{a}**{b}={a**b}")
