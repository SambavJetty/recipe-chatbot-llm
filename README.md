# 🌟 Vertex AI Fine-Tuned Chatbot

A **React.js chatbot** integrated with a **Vertex AI fine-tuned Gemini Flash Lite model**.  
The chatbot streams real-time responses using the [`@ai-sdk/google-vertex`](https://www.npmjs.com/package/@ai-sdk/google-vertex) SDK.

## 📦 Setup Instructions

### 1️⃣ Backend (Flask API)
```bash
# Clone the repository
git clone <your-repo-url>
cd backend
go to the link https://drive.google.com/file/d/1NiHcND1--iINjTFl874D4Sd5Fidix10s/view?usp=sharing and copy the cred.json file and paste in the backend folder as cred.json

# Create virtual environment (Linux/macOS)
python3 -m venv venv
source venv/bin/activate

# Or on Windows
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install flask flask-cors google-genai

# Run the backend
python app.py

Runs on http://localhost:5000


2️⃣ Frontend (React.js)
#open another terminal
cd frontend

# Create React app (if not already created)
npx create-react-app .

# Install dependencies
npm install axios

#Start the frontend server:

npm start

Runs on http://localhost:3000

Open your browser and visit 👉 http://localhost:3000

📝 Example Usage

Sample Input:
milk, sugar, vinegar

Sample Output:
Homemade Hot Chocolate

Ingredients:
- 1 cup Milk
- 1 tbsp Sugar
- 1 tbsp Cocoa Powder

Instructions:
1. Whisk cocoa powder and sugar in a saucepan.
2. Gradually whisk in the milk until smooth.
3. Heat over medium heat, stirring, until hot.
