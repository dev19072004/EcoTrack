import streamlit as st
import google.generativeai as genai

# Configure API Key securely using Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Load Gemini Model
model = genai.GenerativeModel('models/gemini-1.5-flash')

# Function to estimate carbon footprint and provide suggestions
def estimate_carbon_footprint(user_input):
    prompt = f"""
    You are acting as a professional environmental sustainability advisor AI.

    The user has described their typical weekly lifestyle and consumption pattern as follows:
    "{user_input}"

    Analyze this input carefully and perform the following tasks:
    1. Estimate their total weekly carbon footprint in **kilograms of CO₂ equivalent (kg CO₂e)**. Provide an approximate, realistic number based on the activities mentioned.
    2. Identify and explain **the top 2-3 contributors to their emissions**, such as transport, diet, energy use, shopping habits, etc.
    3. Provide at least **3 personalized, actionable suggestions** to help reduce their carbon footprint. Use simple, non-technical language. Keep suggestions practical and realistic (for example, suggest reducing meat intake rather than eliminating it entirely).
    4. Maintain a friendly, non-judgmental tone throughout your advice.

    Output Format:
    - Weekly Carbon Footprint: __ kg CO₂e (approximate)
    - Top Emission Sources:
        1.
        2.
    - Suggestions to Reduce Emissions:
        - Suggestion 1
        - Suggestion 2
        - Suggestion 3
    """

    response = model.generate_content(prompt)
    return response.text.strip()


# Streamlit UI Design
st.set_page_config(page_title="Carbon Footprint Estimator 🌱", page_icon="🌍")

st.title("🌍 Carbon Footprint Estimator AI")
st.markdown("Help fight climate change by understanding your emissions! Describe your lifestyle below and click **Analyze** to receive AI-driven suggestions.")

# Input box
user_input = st.text_area("✍️ Describe your weekly lifestyle, energy use, diet, transport, or shopping habits:")

# Analyze Button
if st.button("♻️ Analyze"):
    if user_input.strip() == "":
        st.warning("Please describe your lifestyle above before analyzing.")
    else:
        with st.spinner("Calculating your carbon footprint..."):
            advice = estimate_carbon_footprint(user_input)

        # Creative Output Styling
        st.success("Here’s your personalized sustainability report:")

        # Use expanders for clarity
        st.markdown("---")
        st.markdown("### 📊 **Your AI-Generated Carbon Footprint Report:**")
        st.markdown(advice.replace("**", "").replace("*", ""))  # Render AI output cleanly

        st.markdown("---")
        with st.expander("💡 Why does this matter?"):
            st.write("""
            Understanding your personal carbon footprint helps you make small changes that collectively have a huge global impact.
            This tool empowers responsible consumption, directly supporting **UN SDG 12** and **Climate Action (SDG 13)**.
            """)

# Footer
st.write("---")
st.caption("Built using Gemini AI & Streamlit • Supporting UN SDG 12 & 13 🌱")
