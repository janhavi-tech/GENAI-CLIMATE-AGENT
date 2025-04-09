def generate_report(article: dict, summary: str, category: str) -> dict:
    return {
        "title": article.get("title", "Untitled"),
        "date": article.get("date", "Not Available"),
        "summary": summary,
        "category": category,
        "url": article.get("url", "URL not available")
    }
