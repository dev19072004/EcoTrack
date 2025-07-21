import google.generativeai as genai

# Step 1: Set your Gemini API Key
api_key = ''
genai.configure(api_key=api_key)

# Step 2: Load Gemini Model
model = genai.GenerativeModel('models/gemini-1.5-flash')

# Step 3: Function to estimate carbon footprint and provide suggestions
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


# Step 4: Continuous loop for user input
while True:
    user_input = input("Describe your lifestyle (or type Exit to quit): ")

    if user_input.lower() == "exit":
        print("Goodbye! Stay sustainable. 🌱")
        break

    advice = estimate_carbon_footprint(user_input)
    print("\n🌍 Estimated Carbon Footprint & Reduction Advice:")
    print(advice)
    print("\n----------------------------------------\n")
