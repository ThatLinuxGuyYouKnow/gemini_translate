import json
import requests

def translateText(request):
    try:
      
        data = request.get_json()
        target_language = data.get("target_language")
        original_language = data.get("original_language")
        text_to_convert = data.get("text")
        api_key = data.get("api_key")

        
        if not all([target_language, original_language, text_to_convert, api_key]):
            return False, {"error": "Missing required fields in the request."}

         
        prompt: str = (
            f"Translate the following text from {original_language} to {target_language}: "
            f"{text_to_convert}. Return the result in JSON format: "
            '{"original_text": "translated_text"}'
        )

         
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ], "generationConfig":{
               "response_mime_type": "application/json",
               "temperature": 0.3,
                "top_p": 1.0
            }
        }

        # Make the API request
        response = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}",
            headers={'Content-Type': "application/json"},
            data=json.dumps(payload)
        )

         
        if response.status_code == 200:
            response_data = response.json()
             
            translated_text =  response_data['candidates'][0]['content']['parts'][0]['text']
            
             
            try:
                translated_result = json.loads(translated_text)
                return True, {
                    "original_text": text_to_convert,
                    "translated_text": translated_result.get("original_text"),
                    "incorrect_original_language": "false"
                }
            except json.JSONDecodeError:
                return False, {"error": "Failed to parse the API response as JSON."}
        else:
             
            return False, {"error": response.text}

    except Exception as e:
     return False, {"error": str(e)}

