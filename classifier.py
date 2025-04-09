def classify_topic(summary: str) -> str:
    summary = summary.lower()

    topics_keywords = {
        "Climate Risk": ["climate risk", "natural disaster", "climate impact", "extreme weather", "sea level", "greenhouse", "climate science"],
        "Policies": ["government", "policy", "regulation", "law", "agreement", "paris agreement", "net zero"],
        "InsureTech": ["insurance", "insurtech", "claims", "underwriting", "risk modeling", "premium", "actuarial"],
        "Sustainability": ["renewable", "sustainability", "solar", "wind", "net zero", "carbon neutral", "clean energy"],
        "Economy & Business": ["market", "finance", "investment", "economic", "business", "corporate", "industry"]
    }

    for topic, keywords in topics_keywords.items():
        if any(keyword in summary for keyword in keywords):
            return topic

    return "Other"
