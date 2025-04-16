import requests

def translateText():
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
            ]
    }
    response = requests.post(f"https://generativelanguage.googleapis.com/v1beta/models/{CONFIG.model}:generateContent?key={apikey}",
        headers={'Content-Type': "application/json"},
        data=json.dumps(payload))