from flask import Flask, render_template, jsonify, request
import json
from pathlib import Path

app = Flask(__name__)

datafile = Path(__file__).parent / "enzymes.json"

# Load enzyme data once at startup
with open(datafile) as f:
    data = json.load(f)
enzymes = data.get("enzymes", [])

summaries = set()
for k in data.keys():
    if k.startswith("summary_"):
        gene_name = k.replace("summary_", "")
        summaries.add(gene_name)

@app.route('/')
def index():
    return render_template('index.html', enzymes=enzymes, summaries=summaries)

@app.route('/enzyme/<gene_name>')
def main_gene_details(gene_name):
    # First, find the enzyme in the main list to verify it exists
    enzyme = next((e for e in summaries), None)
    if not enzyme:
        return "Enzyme not found", 404

    # Get the detailed information for this gene
    if f"gene_{gene_name}" in data.keys():
        gene_key = f"gene_{gene_name}"
        enzyme_detail = data.get(gene_key)

    if f"summary_{gene_name}" in data.keys():
        summary_key = f"summary_{gene_name}"
        summary_detail = data.get(summary_key)

        if enzyme_detail:
            return render_template('gene_details.html', enzyme_details=[summary_detail, enzyme_detail], gene_name=gene_name)

    return "Enzyme details not found 404"


if __name__ == '__main__':
    app.run(debug=True)
