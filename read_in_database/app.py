from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Load enzyme data once at startup
with open('read_in_database/enzymes.json') as f:
    data = json.load(f)
enzymes = data.get("enzymes", [])

@app.route('/')
def index():
    return render_template('index.html', enzymes=enzymes)

@app.route('/enzyme/<gene_name>')
def main_gene_details(gene_name):
    # First, find the enzyme in the main list to verify it exists
    enzyme = next((e for e in enzymes if e.get("gene_name") == gene_name), None)
    if not enzyme:
        return "Enzyme not found", 404

    # Get the detailed information for this gene
    gene_key = f"gene_{gene_name}"
    enzyme_detail = data.get(gene_key)

    if enzyme_detail:
        # Debug print to see the structure
        print(f"Type of enzyme_detail: {type(enzyme_detail)}")
        print(f"Content: {enzyme_detail}")

        return render_template('gene_details.html', enzyme_details=enzyme_detail, gene_name=gene_name)

    return "Enzyme details not found", 404

if __name__ == '__main__':
    app.run(debug=True)