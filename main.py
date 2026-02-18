import feedparser
import os
from groq import Groq

# Initialize the 'Brain'
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def get_trends():
    # Perceptual Layer: Scrape r/Automate and Google News AI trends
    urls = ["https://www.reddit.com/r/automate/hot/.rss", 
            "https://news.google.com/rss/search?q=AI+automation+business"]
    
    all_titles = []
    for url in urls:
        feed = feedparser.parse(url)
        all_titles.extend([entry.title for entry in feed.entries[:3]])
    
    return " | ".join(all_titles)

def generate_viral_script(trends):
    # Reasoning Layer: Plan a Reel script based on trends
    prompt = f"Trends: {trends}\n\nTask: Write a 15-second Instagram Reel script for Kinetic lab Ai. Include a 3-second hook, a mention of $0 overhead automation, and a CTA to 'Comment MOTION' for a demo."
    
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    trends = get_trends()
    script = generate_viral_script(trends)
    print(f"--- TODAY'S KINETIC SCRIPT ---\n{script}")
