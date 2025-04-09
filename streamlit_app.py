import streamlit as st
from summarizer import summarize_article
from classifier import classify_topic

st.title("🌍 Gen-AI Climate Risk News Agent")

# Sample articles for dropdown
examples = {
    "Select an example...": "",
    "🌊 Flood Insurance & Climate Change": """As climate change intensifies, the frequency and severity of floods have increased across the globe. Insurers are now struggling to price flood insurance due to unpredictable patterns. Governments are stepping in with subsidies and new policies to encourage resilience and adaptation.""",
    
    "🔥 Wildfires in California": """Due to prolonged drought and rising temperatures, wildfires in California have become more destructive. Insurance companies have started pulling out of high-risk areas, leaving homeowners with limited options. The state is now reviewing its catastrophe reinsurance strategy.""",
    
    "💡 ESG and InsurTech": """Environmental, Social, and Governance (ESG) principles are reshaping the insurance industry. InsurTech startups are leveraging AI to evaluate climate risk and offer personalized coverage. This shift aims to address both customer demand and regulatory pressure."""
}

# Dropdown to choose an example
selected_example = st.selectbox("💬 Try with a sample article:", list(examples.keys()))

# Autofill textarea when dropdown is selected
if selected_example and examples[selected_example]:
    article_text = st.text_area("Paste article text:", examples[selected_example])
else:
    article_text = st.text_area("Paste article text:")

# Process article
if st.button("Summarize & Classify"):
    if not article_text.strip():
        st.warning("Please enter or select an article text to continue.")
    else:
        summary = summarize_article(article_text)
        category = classify_topic(summary)

        st.markdown(f"### 📝 Summary:\n{summary}")
        st.markdown(f"### 🏷️ Category: `{category}`")
