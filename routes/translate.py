import requests

def translateText(request):
    data = request.get_json()
    target_language = data.get("target_language")
    original_language = data.get("original_language")
    text_to_convert = data.get("text")
    api_key = data.get("api_key")
    prompt: str = f""" 
Convert the text {text_to_convert} from {original_language} to {target_language}. If the"""
    payload = {
          "system_instruction": {
                "parts": [
                    {
                        "text": "You are a language translation expert, you will accuratley convert the text provided to the stated language"
                    }
                ]
            },
            "contents": [
                {
                    "parts": [
                        {
                            "text": prompt
                            
                        }
                    ]
                }
            ],
            "generationConfig":"application/json"
    }
    response = requests.post(f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash/generateContent?key={api_key}",
        headers={'Content-Type': "application/json"},
        data=json.dumps(payload))