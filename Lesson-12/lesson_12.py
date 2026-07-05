import random
import string
import secrets


def random_user_id(length=6):
    ch = string.ascii_letters + string.digits
    user_id = ''.join(secrets.choice(ch)for _ in range(length))
    return user_id


def user_id_gen_by_user():
    id_num = int(input("Enter the number of IDs you want to generate: "))
    id_length = int(input("Enter the length of each ID: "))
    if id_num <= 0 or id_length <= 0:
        return "Please enter a positive number for both id_num and id_length."
    ids = []
    for i in range(id_num):
        ids.append(random_user_id(id_length))
    for j in range(id_num):
        print(ids[j])


print(user_id_gen_by_user())


def rgb_colour_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"


def list_of_hexa_colours(length):
    hex = string.hexdigits
    hex_colours = []
    for i in range(length):
        colour = "#"+"".join(random.choices(hex, k=6))
        hex_colours.append(colour)
    return hex_colours


def list_of_rgb_colours(length):
    rgb_lst = []
    for i in range(length):
        rgb_lst.append(rgb_colour_gen())
    return rgb_lst


def generate_colours(colour, length):
    if str(colour).lower() == "hexa":
        return list_of_hexa_colours(length)
    elif str(colour).lower() == "rgb":
        return list_of_rgb_colours(length)
    else:
        return "Please enter a valid colour type: 'hexa' or 'rgb'."


def shuffle_list(lst):
    random.shuffle(lst)
    return lst


def random_number():
    arr = random.choices(range(10), k=7)
    return arr


print(generate_colours("hexa", 5))
print(generate_colours("rgb", 4))
print(shuffle_list([1, 2, 3, 4, 5]))
print(random_number())
