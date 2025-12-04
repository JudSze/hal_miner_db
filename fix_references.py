import json
import re

pattern="doi.*[a-zA-Z0-9],|doi.*[a-zA-Z0-9]"
updated_enzymes = {"enzymes": []}

with open("/home/szenei/hal_miner_db/read_in_database/enzymes_copy.json", "r") as db:
    data=json.load(db)
    for entry in data["enzymes"]:
        if type(entry["reference"]) != list:
            res=re.findall(pattern, entry["reference"])
            entry["reference"] = list(res)
        updated_enzymes["enzymes"].append(entry)
    with open("/home/szenei/hal_miner_db/read_in_database/updated_enzymes.json", "w") as updated_enzymes_db:
        json.dump(updated_enzymes, updated_enzymes_db)




