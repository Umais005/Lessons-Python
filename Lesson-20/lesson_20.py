import requests
from collections import Counter
import re
import statistics
import bs4

url = "https://www.gutenberg.org/cache/epub/1513/pg1513-images.html"
response = requests.get(url)

if response.status_code == 200:
    text = response.text
    words = re.findall(r"\b\w+\b", text.lower())
    count = Counter(words)
    print(count.most_common(10))
else:
    print("Failed to fetch text")

url1 = "https://api.thecatapi.com/v1/breeds"
res1 = requests.get(url1)
if res1.status_code == 200:
    cats = res1.json()

    weights = []
    lifespan = []
    origins = []

    for breed in cats:
        weight_str = breed.get("weight", "{}").get("metric", "")
        if "-" in weight_str:
            min_w, max_w = map(float, weight_str.split("-"))
            weights.append((min_w+max_w)/2)

        life_str = breed.get("life_span", "")
        if "-" in life_str:
            min_l, max_l = map(float, life_str.split("-"))
            lifespan.append((min_l+max_l)/2)

        origins.append(breed.get("origin", "Unknown"))

    def print_stats(name, data_list):
        print(f"----{name}---")
        print(f"Min: {min(data_list):.2f}")
        print(f"Max: {max(data_list):.2f}")
        print(f"Mean: {statistics.mean(data_list):.2f}")
        print(f"Median: {statistics.median(data_list):.2f}")
        print(f"Standard Deviation: {statistics.stdev(data_list):.2f}")

    print_stats("Cat Weights", weights)
    print_stats("Cat Life Span", lifespan)

    print("---Frequency Table---")
    o_count = Counter(origins)
    for country, count in o_count.most_common():
        print(f"{country}: {count} breeds")
else:
    print("FAILURE!")

url2 = "https://archive.ics.uci.edu/"

res2 = requests.get(url2)
soup = bs4.BeautifulSoup(res2.text, "html.parser")
tables = soup.find_all("table")
print(f"{len(tables)} tables found!")
print("\nFirst 5 dataset links: ")

links = soup.find_all("a", href=True)
count = 0
for link in links:
    href = link["href"]
    if "datasets/" in href or "dataset/" in href:
        print(f"Text: {link.text.strip()} | URL: {href}")
        count += 1
        if count >= 5:
            break
