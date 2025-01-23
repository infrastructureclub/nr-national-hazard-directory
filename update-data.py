#!/usr/bin/python
import os
import requests
import json
import base64

BASE_URL = "https://nhd-prd-api.on-trac.co.uk/nhd/api"

token = os.getenv("TOKEN")

response = requests.get(
    f"{BASE_URL}/data/route/all", headers={"nhd-access-points-mobile": token}
)
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

datasets = ("coreData", "elrLookup")
for region in regions:
    code = region["zonecode"]
    os.makedirs(f"data/{code}", exist_ok=True)

    for dataset in datasets:
        print(f"Fetching {code} {dataset} data")
        response = requests.get(
            f"{BASE_URL}/external/accessPoint/{dataset}/{code}",
            headers={"nhd-access-points-mobile": token},
        )

        if response.status_code != 200:
            raise Exception("Fetch failed")

        with open(f"data/{code}/{dataset}.csv", "w", encoding="ISO-8859-1") as f:
            f.write(response.content.decode("ISO-8859-1"))
