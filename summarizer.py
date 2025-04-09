
# summarizer.py
import google.generativeai as genai

# ✅ Replace with your actual Google API Key
genai.configure(api_key="google_api_key")
model = genai.GenerativeModel("models/gemini-1.5-pro") 

def summarize_article(content):
    try:
        prompt = f"Summarize the following article in 3 to 5 lines:\n\n{content}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("Error while summarizing:", e)
        return "Summary not available due to an error."
