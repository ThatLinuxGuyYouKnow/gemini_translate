from flask import Flask, request, jsonify
from flask_cors import CORS

from routes.translate import translateText

app = Flask(__name__)
 
CORS(app)  

@app.route('/translate')
def translation_route():
    translateText(request)