# lesson 19
from collections import Counter
import json
import re
import os
import math
import csv


def find_lines_and_word(ff):
    content = ff.read()
    lines = content.splitlines()
    words = content.split()
    print(f"No. of lines are: {len(lines)} and words are: {len(words)}")
    return len(lines), len(words)


with open(r"C:\Users\moona\30-Lessons-Python\Lesson-19\michelle_obama_speech.txt", encoding="utf-8") as f:
    find_lines_and_word(f)

with open(r"C:\Users\moona\30-Lessons-Python\Lesson-19\obama_speech.txt", encoding="utf-8") as g:
    find_lines_and_word(g)

with open(r"C:\Users\moona\30-Lessons-Python\Lesson-19\donald_speech.txt", encoding="utf-8") as h:
    find_lines_and_word(h)

with open(r"C:\Users\moona\30-Lessons-Python\Lesson-19\melina_trump_speech.txt", encoding="utf-8") as i:
    find_lines_and_word(i)


def most_populated_countries(n, j=r"C:\Users\moona\30-Lessons-Python\Lesson-19\countries_data.json"):
    with open(j, "r", encoding="utf-8") as file:
        data = json.load(file)
    sorted_countries = sorted(
        data, key=lambda x: x.get("population", 0), reverse=True)
    top_countries = [{"country": country["name"], "population": country["population"]}
                     for country in sorted_countries[:n]]
    return top_countries


print(most_populated_countries(
    10, j=r"C:\Users\moona\30-Lessons-Python\Lesson-19\countries_data.json"))


def most_spoken_languages(n, j=r"C:\Users\moona\30-Lessons-Python\Lesson-19\countries_data.json"):
    with open(j, "r", encoding="utf-8") as file:
        data = json.load(file)
    all_lang = []
    all_lang.extend(lang for country in data for lang in country["languages"])
    count = Counter(all_lang)
    return count.most_common(n)


print(most_spoken_languages(
    10, j=r"C:\Users\moona\30-Lessons-Python\Lesson-19\countries_data.json"))


def extract_emails(file=r"C:\Users\moona\30-Lessons-Python\Lesson-19\email.txt"):
    email_address = set()

    email_pattern = r"^From:\s+(\S+@\S+)"

    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(email_pattern, line)
            if match:
                email_address.add(match.group(1))
    return sorted(list(email_address))


inc_email = extract_emails()
print(f"Found {len(inc_email)} unique email addresses.")
print(inc_email[:5])


def find_mc_words(n, ff):
    with open(ff, "r", encoding="utf-8") as f:
        text = f.read()
    words = re.findall(r"[a-zA-Z]+", text)
    count = Counter(words).most_common(n)
    result = [(c, item) for item, c in count]
    return result


print(find_mc_words(
    10, r"C:\Users\moona\30-Lessons-Python\Lesson-19\michelle_obama_speech.txt"))
print(find_mc_words(10, r"C:\Users\moona\30-Lessons-Python\Lesson-19\obama_speech.txt"))
print(find_mc_words(10, r"C:\Users\moona\30-Lessons-Python\Lesson-19\donald_speech.txt"))
print(find_mc_words(
    10, r"C:\Users\moona\30-Lessons-Python\Lesson-19\melina_trump_speech.txt"))


def cleaned_text(text):
    text = text.lower()
    clean = re.sub(r"[^a-z0-9\s]", "", text)
    return clean


def input_w(txt_pth):
    if isinstance(txt_pth, str) and os.path.isfile(txt_pth):
        with open(txt_pth, "r", encoding="utf-8") as f:
            return f.read()
    return str(txt_pth)


def remove_sw(ct, stop_word):
    w = ct.split()
    m_words = [word for word in w if word not in stop_word]
    return m_words


def similarity(input1, input2):
    t1 = input_w(input1)
    t2 = input_w(input2)
    stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up',
                  'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    clean1 = cleaned_text(t1)
    clean2 = cleaned_text(t2)

    words_1 = remove_sw(clean1, stop_words)
    words_2 = remove_sw(clean2, stop_words)

    v1 = Counter(words_1)
    v2 = Counter(words_2)

    intersection = set(v1.keys()) & set(v2.keys())
    numerator = sum([v1[x]*v2[x] for x in intersection])
    s1 = sum([v1[x]**2 for x in list(v1.keys())])
    s2 = sum([v2[x]**2 for x in list(v2.keys())])
    denom = math.sqrt(s1)*math.sqrt(s2)

    if not denom:
        return 0.0

    ss = float(numerator)/denom
    return ss*100


score = similarity(r"C:\Users\moona\30-Lessons-Python\Lesson-19\michelle_obama_speech.txt",
                   r"C:\Users\moona\30-Lessons-Python\Lesson-19\melina_trump_speech.txt")
print(f"similarity percentage is {score:.2f}%")

print(find_mc_words(
    10, r"C:\Users\moona\30-Lessons-Python\Lesson-19\romeo_and_juliet.txt"))
