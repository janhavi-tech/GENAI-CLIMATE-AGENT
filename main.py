from scraper import scrape_articles
from summarizer import summarize_article
from classifier import classify_topic
from report_generator import generate_report

if __name__ == "__main__":
    urls = [
        "https://www.reuters.com/business/environment/",
        "https://www.theguardian.com/environment/climate-crisis",
        "https://www.insurancebusinessmag.com/us/tag/climate-risk/",
        "https://climate.nasa.gov/news/",
        "https://www.businessinsurance.com/section/climate-change"
    ]

    print("🔍 Scraping climate-related articles...")
    articles = scrape_articles(urls)
    print(f"✅ Found {len(articles)} articles.")

    final_reports = []

    for idx, article in enumerate(articles, start=1):
        print(f"\n📄 Processing Article {idx}: {article.get('title', 'Untitled')}")

        try:
            summary = summarize_article(article['content'])
        except Exception as e:
            print(f"❌ Error during summarization: {e}")
            summary = "Summary not available due to an error."

        try:
            category = classify_topic(summary)
        except Exception as e:
            print(f"⚠️ Error during classification: {e}")
            category = "Other"

        report = generate_report(article, summary, category)
        final_reports.append(report)

    print("\n📑 Final Reports:\n")
    for r in final_reports:
        print("\n--- Report ---")
        print(f"Title: {r.get('title', 'N/A')}")
        print(f"Date: {r.get('date', 'N/A')}")
        print(f"Category: {r.get('category', 'N/A')}")
        print(f"Summary: {r.get('summary', 'N/A')}")
        print(f"Source: {r.get('url', 'N/A')}")
