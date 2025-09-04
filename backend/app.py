from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from google.genai import types
import google.auth
from google.oauth2 import service_account
import os

app = Flask(__name__)
CORS(app)

# Service Account Authentication
SERVICE_ACCOUNT_FILE = 'cred.json'  # Keep this secure!

# Setup Vertex AI Client with service account
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=['https://www.googleapis.com/auth/cloud-platform']
)

client = genai.Client(
    vertexai=True,
    project="609219926595",
    location="us-central1",
    credentials=credentials
)

MODEL_ENDPOINT = "projects/609219926595/locations/us-central1/endpoints/3692972585164734464"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_message = data.get("message")

        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=user_message)]
            )
        ]

        config = types.GenerateContentConfig(
            temperature=0.7,
            max_output_tokens=512,
            top_p=0.9,
            safety_settings=[
                types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="OFF"),
                types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="OFF"),
                types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="OFF"),
                types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="OFF"),
            ]
        )

        response_text = ""
        for chunk in client.models.generate_content_stream(
            model=MODEL_ENDPOINT,
            contents=contents,
            config=config,
        ):
            if chunk.text:
                response_text += chunk.text

        return jsonify({"reply": response_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)