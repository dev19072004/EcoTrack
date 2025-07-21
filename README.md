
EcoTrack: AI-Powered Carbon Footprint Estimator 🌍🌱
===================================================

EcoTrack is a Streamlit web app that estimates a user's weekly carbon footprint based on their lifestyle.
It uses Google's Gemini AI model to provide practical, non-technical suggestions to reduce carbon emissions,
supporting the goals of UN SDG 12 (Responsible Consumption) and SDG 13 (Climate Action).

🔗 LIVE APP
-----------
🌐 Try the app here: https://ecotracker.streamlit.app/

🔧 Features
----------
- Natural language input for describing lifestyle (diet, transport, energy use, etc.)
- AI-generated weekly carbon footprint estimation in kg CO₂e
- Top 2-3 emission sources identified
- Personalized suggestions to reduce emissions
- Clean, interactive Streamlit UI with buttons, expanders, and styled output

🧠 Powered By
-------------
- Google Gemini (Generative AI) via `google-generativeai`
- Streamlit for frontend interaction
- Streamlit Cloud (optional) for deployment

📁 Files
-------
- `app.py`: Main Streamlit app
- `requirements.txt`: Python dependencies

🚀 How to Run Locally
---------------------
1. Install dependencies:
   pip install -r requirements.txt

2. Create a `.streamlit/secrets.toml` file with your Gemini API key:
   [example]
   GEMINI_API_KEY = "your-api-key-here"

3. Run the app:
   streamlit run app.py

🌐 How to Deploy on Streamlit Cloud
-----------------------------------
1. Push your code to GitHub
2. Go to https://streamlit.io/cloud
3. Connect your GitHub repo
4. Add your `GEMINI_API_KEY` under the Secrets tab
5. Click "Deploy"

👨‍💻 Author
----------
Created by Devanshu Verma (2025)

🛡️ License
---------
MIT License (if open-sourced)

🌿 Let's build a greener future with AI!
