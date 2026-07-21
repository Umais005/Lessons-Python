import json
from bs4 import BeautifulSoup
import re
import requests

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
c1 = response.content
table_data = []
if response.status_code == 200:
    sp = BeautifulSoup(c1, "html.parser")
    tables = sp.find_all("table")
    for tbl_idx, tbl in enumerate(tables):
        rows = tbl.find_all("tr")
        tbl_row = []
        for row in rows:
            cols = row.find_all(["th", "td"])
            cols_txt = [ele.get_text(strip=True) for ele in cols]
            if cols_txt:
                tbl_row.append(cols_txt)
        if tbl_row:
            table_data.append({
                "table_index": tbl_idx,
                "rows": tbl_row
            })

    output_dict = {
        "source_url": url,
        "status": "success",
        "tables_extracted": len(table_data),
        "data": table_data
    }
else:
    output_dict = {
        "source_url": url,
        "status": "failed",
        "error_code": response.status_code
    }

o_file3 = r"C:\Users\moona\30-Lessons-Python\Lesson-22\presidents.json"
with open(o_file3, "w", encoding="utf-8") as f3:
    json.dump(output_dict, f3, indent=4, ensure_ascii=False)
    print(f"Table data successfully extrated and saved to {o_file3}")
