numbers = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pos_num = [n for n in numbers if n > 0]
print(pos_num)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = [num for sub in list_of_lists for num in sub]
print(flat_list)

list_comp = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(list_comp)

countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flat_list = [(country.upper(), country[0:3].upper(), capital.upper())
             for sub in countries for country, capital in sub]
print(flat_list)

dic_list = [{"country": country, "city": city}
            for sub in countries for country, city in sub]
print(dic_list)

names = [[('Muhammad', 'Umais')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]

flat_names = [i + ' ' + j for sub in names for i, j in sub]
print(flat_names)


def slope(x1, x2, y1, y2):
    return (y2 - y1) / (x2 - x1)


print(slope(1, 2, 3, 4))
