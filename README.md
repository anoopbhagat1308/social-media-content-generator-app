# 🤖 AI Social Media Content Generator

An AI-powered Streamlit application that generates engaging social media
content using Google's Gemini API.

## 🚀 Features

-   Generate content for:
    -   LinkedIn
    -   X (Twitter)
    -   Instagram
    -   Facebook
-   Select content tone:
    -   Professional
    -   Friendly
    -   Educational
    -   Motivational
    -   Humorous
-   Choose content length (Short, Medium, Long)
-   Optional emojis and hashtags
-   AI-generated hook, body, CTA, and hashtags

## 🛠️ Tech Stack

-   Python
-   Streamlit
-   Google GenAI SDK
-   Gemini 3.1 Flash Lite
-   python-dotenv
-   Git & GitHub
-   Streamlit Community Cloud

## 📁 Project Structure

``` text
social-media-content-generator/
│── app.py
│── ai_generator.py
│── requirements.txt
│── .env.example
│── .gitignore
│── README.md
```

## ⚙️ Installation

``` bash
git clone https://github.com/your-username/social-media-content-generator.git
cd social-media-content-generator
pip install -r requirements.txt
```

Create a `.env` file:

``` text
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

Run the application:

``` bash
streamlit run app.py
```

## ☁️ Deployment

1.  Push the project to GitHub.
2.  Deploy using Streamlit Community Cloud.
3.  Add the API key under **App Settings → Secrets**:

``` toml
GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
```

## 📸 Application Workflow

1.  Enter a topic.
2.  Choose platform, tone, and content length.
3.  Select whether to include emojis and hashtags.
4.  Click **Generate Content**.
5.  AI generates a ready-to-post social media post.

## 📌 Future Enhancements

-   Copy to clipboard
-   Download as PDF/TXT
-   30-day content calendar
-   Multi-language support
-   AI image prompt generation
-   Content history

## 👨‍💻 Author

**Anoop Bhagat**

If you found this project useful, consider giving it a ⭐ on GitHub.
