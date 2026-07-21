import json
import requests
from bs4 import BeautifulSoup
import re

url1 = 'http://www.bu.edu/president/boston-university-facts-stats/'
headers = {"User-Agent": "Mozilla/5.0"}
response1 = requests.get(url1, headers=headers)
c1 = response1.content
scraped_data = {}
if response1.status_code == 200:
    sp1 = BeautifulSoup(c1, "html.parser")
    sections = []
    for heading in sp1.find_all(["h2", "h3", "h4"]):
        section_title = heading.get_text(strip=True)
        content = []

        sibling = heading.find_next_sibling()
        while sibling and sibling.name not in ["h2", "h3", "h4"]:
            text = sibling.get_text(strip=True)
            if text:
                content.append(text)
            sibling = sibling.find_next_sibling()

        if content:
            sections.append({
                "heading": section_title,
                "content": content
            })

        scraped_data = {
            "url": url1,
            "status": "success",
            "sections": sections
        }

else:
    scraped_data = {
        "url": url1,
        "status": "failed",
        "error_code": response1.status_code
    }

o_file = r"C:\Users\moona\30-Lessons-Python\Lesson-22\bu_facts.json"
with open(o_file, "w", encoding="utf-8") as f:
    json.dump(scraped_data, f, indent=4, ensure_ascii=False)
    print(f"Data successfully scraped and saved to {o_file}")


url2 = "https://archive.ics.uci.edu/dataset/53/iris"
headers = {"User-Agent": "Mozilla/5.0"}
response2 = requests.get(url2, headers=headers)
table_data = []
if response2.status_code == 200:
    sp2 = BeautifulSoup(response2.text, "html.parser")
    tables = sp2.find_all("table")
    for table_idx, tbl in enumerate(tables):
        rows = tbl.find_all("tr")
        tbl_rows = []
        for row in rows:
            cols = row.find_all(["th", "td"])
            cols_txt = [ele.get_text(strip=True)for ele in cols]
            if cols_txt:
                tbl_rows.append(cols_txt)

        if tbl_rows:
            table_data.append({
                "table_index": table_idx,
                "rows": tbl_rows
            })

    output_dict = {
        "source_url": url2,
        "status": "success",
        "tables_extracted": len(table_data),
        "data": table_data
    }
else:
    output_dict = {
        "source_url": url2,
        "status": "failed",
        "error_code": response2.status_code
    }

o_file2 = r"C:\Users\moona\30-Lessons-Python\Lesson-22\uci_tbles.json"
with open(o_file2, "w", encoding="utf-8") as f2:
    json.dump(output_dict, f2, indent=4, ensure_ascii=False)
    print(f"Table data successfully extrated and saved to {o_file2}")
