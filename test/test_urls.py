import json
import requests

references_path = "/home/szenei/hal_miner_db/read_in_database/enzymes.json"

def validate_references(ref_path):
    correct_links = []
    incorrect_links = []

    with open(ref_path) as enzymes_d:
        enzymes = json.load(enzymes_d)

        genes_summaries = {gene: enzymes[gene] for gene in enzymes if gene != "enzymes"}
        for enzyme, details_l in genes_summaries.items():
            for details in details_l:
                try:
                    reference = details.get("reference")
                    for link in reference:
                        try:
                            response = requests.get(f"https://doi.org/{link}")
                            if response.status_code == 200 or response.status_code == 403:
                                correct_links.append(enzyme)
                            else:
                                incorrect_links.append((enzyme, link))
                                print(enzyme, link)
                        except Exception:
                            incorrect_links.append((enzyme, link))
                except TypeError:
                    print(f"No reference for {enzyme}")

    return correct_links, incorrect_links

correct_references, incorrect_references = validate_references(references_path)
