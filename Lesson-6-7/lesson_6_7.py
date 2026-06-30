it_companies = set()
it_companies.add("Twitter")
it_companies.update(["Facebook", "Instagram", "LinkedIn"])
it_companies.remove("Twitter")

print(it_companies)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a.union(b))

print(a.issubset(b))

print(a.intersection(b))


print(a.symmetric_difference(b))

del a
del b

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

s_ages = set(ages)

print(len(ages))
print(len(s_ages))

string = "I am a teacher and I love to inspire and teach people"
words = string.split()
s_words = set(words)
print(words)
print(s_words)
