from flask import Flask, request, jsonify
from abstractive import abstractive_summary

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get("text", "")
    summary = abstractive_summary(text)
    return jsonify({"summary": summary})

if __name__ == '__main__':
    app.run(debug=True)
