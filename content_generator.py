import os
from dotenv import load_dotenv
import streamlit as st
from google import genai

# Load .env file
load_dotenv()

# Get API Key
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except Exception:
    api_key = os.getenv("GOOGLE_API_KEY")

# Create Gemini Client
client = genai.Client(api_key=api_key)


def generate_content(topic, platform, tone, length, emoji, hashtags):

    prompt = f"""
    You are an expert social media content creator.

    Generate a {length} social media post.

    Topic:
    {topic}

    Platform:
    {platform}

    Tone:
    {tone}

    Include Emojis:
    {"Yes" if emoji else "No"}

    Include Hashtags:
    {"Yes" if hashtags else "No"}

    Requirements:
    - Start with a catchy hook.
    - Write engaging content.
    - Keep it suitable for {platform}.
    - End with a strong Call-to-Action.
    """

    response = client.models.generate_content(
        model="models/gemini-3.1-flash-lite",
        contents=prompt
    )

    return response.text