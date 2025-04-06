import gemini_text_analysis

from flask import Flask, jsonify

app = Flask(__name__)

locations = gemini_text_analysis.prompt_json()

@app.route('/api/locations')
def get_locations():
    return jsonify(locations)

if __name__ == '__main__':
    app.run(debug=True)

