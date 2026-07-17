import streamlit as st
from content_generator import generate_content

st.set_page_config(
    page_title="AI Social Media Content Generator",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Social Media Content Generator")

topic = st.text_input("Enter Topic")

platform = st.selectbox(
    "Select Platform",
    ["LinkedIn", "Twitter (X)", "Instagram", "Facebook"]
)

tone = st.selectbox(
    "Select Tone",
    ["Professional", "Friendly", "Educational", "Motivational", "Humorous"]
)

length = st.selectbox(
    "Content Length",
    ["Short", "Medium", "Long"]
)

emoji = st.checkbox("Include Emojis")

hashtags = st.checkbox("Include Hashtags")

if st.button("Generate Content"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:

        with st.spinner("Generating content..."):

            output = generate_content(
                topic,
                platform,
                tone,
                length,
                emoji,
                hashtags
            )

        st.subheader("Generated Content")

        st.markdown(output)