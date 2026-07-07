# 18

import re
from collections import Counter


paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."


words = re.findall(r"\b\w+\b", paragraph, re.I)
wordcount = (Counter(words))
m_frequent, count = wordcount.most_common(1)[0]

print(f"The most frequent word is {m_frequent} with {count} occurences")


def valid_variable(var):
    pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
    return bool(re.match(pattern, var))


print(valid_variable('first_name'))   # True
print(valid_variable('first-name'))   # False (Contains a hyphen)
print(valid_variable('1first_name'))  # False (Starts with a number)
print(valid_variable('firstname'))   # True
print(valid_variable('_variable'))

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

clean_sentence = re.sub(r"[^a-zA-Z0-9.\s]", "", sentence)
print(clean_sentence)

w = clean_sentence.split()
w_count = Counter(w)

three = w_count.most_common(3)
