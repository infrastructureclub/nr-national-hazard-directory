#!/usr/bin/python
import os
import requests
import json

token = os.getenv("TOKEN")

response = requests.get(f"http://mobile.nationalhazards.co.uk/regions?token={token}")
regions = json.loads(response.content)

os.makedirs("data", exist_ok=True)
with open("data/regions.json", "w") as f:
    f.write(
        json.dumps(
            regions,
            indent=4,
            sort_keys=True,
            separators=(",", ": "),
            ensure_ascii=False,
        )
    )

datasets = ("core_data", "elr_lookup", "freetext", "subzone_code", "subzone_lookup")
for code, name in regions.items():
    os.makedirs(f"data/{code}", exist_ok=True)

    for dataset in datasets:
        print(f"Fetching {code}/{dataset}")
        response = requests.get(
            f"http://mobile.nationalhazards.co.uk/regions/{code}/{dataset}?token={token}"
        )

        if response.status_code != 200:
            raise Exception("Fetch failed")

        with open(f"data/{code}/{dataset}.csv", "w", encoding="ISO-8859-1") as f:
            f.write(response.content.decode("ISO-8859-1"))
