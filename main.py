from flask import Flask, request, jsonify
from flask_cors import CORS

from routes.translate import translateText

app = Flask(__name__)
 
CORS(app)  

@app.route('/translate', methods = ['POST'])
def translation_route():
    status,response = translateText(request)
    if status:
       return jsonify(response),200
    else: 
    
 
     return False, {"error": response.text or "Empty response from translation API"}
