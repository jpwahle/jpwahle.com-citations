# scripts/build_json.py  (≈15 lines)
import json
import sys
import serpapi

key, author = sys.argv[1:3]
data = serpapi.search(
    {"engine": "google_scholar_author", "author_id": author, "api_key": key}
)

out = {
    "total": data["cited_by"]["table"][0]["citations"]["all"],
    "h_index": data["cited_by"]["table"][1]["h_index"]["all"],
    "i10_index": data["cited_by"]["table"][2]["i10_index"]["all"],
    "year_graph": data["cited_by"]["graph"],  # array of {year,value}
}
with open("citations.json", "w") as f:
    json.dump(out, f, indent=2)
