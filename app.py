from flask import Flask, render_template, request
from tpb import TPB, CATEGORIES, ORDERS

app = Flask(__name__)
t = TPB('https://thepiratebay.org')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    results = t.search(query)
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
