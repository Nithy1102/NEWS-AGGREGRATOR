from flask import Flask, jsonify, request,render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

NEWS_API_KEY = '6ce8881d68f24f5bb1f7549cd71056f1'
BASE_URL = 'https://newsapi.org/v2/top-headlines'



@app.route('/news', methods=['GET'])
def get_news():
    category = request.args.get('category', 'general')
    params = {
        'apiKey': NEWS_API_KEY,
        'country': 'us',
        'category': category,
        'pageSize': 20
    }
    response = requests.get(BASE_URL, params=params)
    
    # Debugging output
    print("Request sent to NewsAPI:", response.url)
    print("Status code:", response.status_code)
    print("Response JSON:", response.text[:200])  

    return jsonify(response.json())


if __name__ == '__main__':
    app.run(debug=True)
