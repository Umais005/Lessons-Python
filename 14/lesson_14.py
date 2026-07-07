# 14
from functools import reduce
from collections import Counter, deque
from countriesdata import countries as c_s

countriess = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cabo Verde',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombia',
    'Comoros',
    'Congo, Democratic Republic of the',
    'Congo, Republic of the',
    'Costa Rica',
    "Côte d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor-Leste)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Eswatini',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Montenegro',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'North Macedonia',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Palestine',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent and the Grenadines',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'South Sudan',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Sweden',
    'Switzerland',
    'Syria',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe'
]
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

upper_countries = map(lambda country: country.upper(), countries)
print(list(upper_countries))

square = map(lambda num: num**2, numbers)
print(list(square))

upper_names = map(lambda name: name.upper(), names)
print(list(upper_names))


def without_land(country):
    if "land" not in country:
        return True
    return False


w_land = filter(without_land, countries)
print(list(w_land))


def six(country):
    if len(country) == 6:
        return True
    return False


six_char = filter(six, countries)
print(list(six_char))


def m_six(country):
    if len(country) >= 6:
        return True
    return False


m_six_char = filter(m_six, countries)
print(list(m_six_char))


def e_begin(country):
    if country.startswith("E"):
        return True
    return False


e_begin_char = filter(e_begin, countries)
print(list(e_begin_char))

result = reduce(lambda x, y: x+y, filter(lambda x: x %
                2 == 0, map(lambda x: x**2, numbers)))
print(result)


def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))


print(get_string_lists([1, 2, 3, 'a', 'b', 'c']))

sum = reduce(lambda x, y: x+y, numbers)
print(sum)

sentence = reduce(lambda x, y: x+", "+y, countries)
print(sentence)


def diction(coun):
    f_letters = map(lambda x: x[0].upper(), coun)
    return dict(Counter(f_letters))


print(diction(countriess))


queue = deque(countriess)

f_10 = reduce(lambda x, y: x+", "+y,
              map(lambda x: x.upper(), [queue.popleft() for _ in range(10)]))
print(f_10)

l_10 = reduce(lambda x, y: x+", "+y,
              map(lambda x: x.upper(), [queue.pop() for _ in range(10)]))
print(l_10)


def sort_c(c):
    return sorted(c, key=lambda x: x['name'])


print(sort_c(c_s))


def sort_cap(c):
    return sorted(c, key=lambda x: x.get('capital', ''))


print(sort_cap(c_s))


def sort_pop(c):
    return sorted(c, key=lambda x: x['population'], reverse=True)


print(sort_pop(c_s))


def sort_area(c):
    return sorted(c, key=lambda x: x['population'], reverse=True)[:10]


print(sort_area(c_s))


def sort_languages(c):
    all_lang = []
    for country in c:
        all_lang.extend(country["languages"])

    count = Counter(all_lang)
    return count.most_common(10)


print(sort_languages(c_s))
