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
    enzyme = next((e for e in enzymes if e.get("gene_name") == gene_name), None)
    if enzymes:
        return render_template('gene_details.html', enzyme=enzyme)
    return "Enzyme not found", 404

@app.route('/enzyme_detail')
def enzyme_details(gene_name):
    for enzyme in enzymes:
        enzyme_detail = data.get(f"gene_{enzyme["gene_name"]}")
        if enzyme_detail:
            return render_template('gene_details.html', enzyme=enzyme_detail)
    return "Enzyme not found", 404

if __name__ == '__main__':
    app.run(debug=True)
