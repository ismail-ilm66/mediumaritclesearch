from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Read the CSV file into DataFrame
data = pd.read_csv('data2.csv')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search():
    # Get the search query from the request
    query = request.args.get('query')

    # Perform the search
    results = data[data['Title'].str.contains(query, case=False)]

    # Convert the results to JSON
    json_results = results.to_json(orient='records')

    return json_results


if __name__ == '__main__':
    app.run(debug=True)
