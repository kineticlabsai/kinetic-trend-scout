import praw
import os
from openai import OpenAI

# 1. Setup Reddit API (Scout)
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="TrendScout 1.0"
)

# 2. Setup LLM (Brain)
client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=os.getenv("GROQ_API_KEY"))

def get_trends():
    subreddit = reddit.subreddit("automate")
    trends = [post.title for post in subreddit.hot(limit=5)]
    return " | ".join(trends)

def generate_script(trends):
    prompt = f"Based on these trends: {trends}, write a 15-second Instagram Reel script for Kinetic lab Ai. Include a 3-second hook, a mention of '$0 overhead,' and a CTA to 'Comment MOTION'."
    
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    current_trends = get_trends()
    viral_script = generate_script(current_trends)
    print(f"--- VIRAL SCRIPT FOR KINETIC LAB AI ---\n{viral_script}")
