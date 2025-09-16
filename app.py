import streamlit as st
import google.generativeai as genai
import os

# --- Configuration ---
# Set page configuration for a more professional look
st.set_page_config(
    page_title="Content Augmentation with Gemini",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Styling ---
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        padding: 10px 24px;
        border: none;
        font-size: 16px;
        transition-duration: 0.4s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextArea textarea {
        border-radius: 12px;
        border: 2px solid #ddd;
        padding: 10px;
    }
    .stTextInput input {
        border-radius: 12px;
        border: 2px solid #ddd;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)


# --- Main Application ---
st.title("📝 Content Augmentation Engine")
st.markdown("Expand and refine your content using the power of the Gemini 2.5 Pro API. Simply provide your original text and the strategic goals, and let the AI do the rest.")


# --- Sidebar for Inputs ---
with st.sidebar:
    st.header("⚙️ Configuration")
    st.markdown("Enter your API key and content parameters below.")

    # Get Gemini API key from user
    # This section handles the API key securely.
    # When deployed on Streamlit Community Cloud, it uses the st.secrets functionality.
    # When running locally, it falls back to a password input field.
    if hasattr(st, 'secrets') and 'GEMINI_API_KEY' in st.secrets:
        api_key = st.secrets['GEMINI_API_KEY']
        st.success("API Key loaded from secrets!", icon="✅")
    else:
        api_key = st.text_input("Enter your Gemini API Key:", type="password", help="You can get your API key from [Google's AI Studio](https://makersuite.google.com/app/apikey).")

    st.header("🎯 Content Strategy")
    primary_topic = st.text_input("Primary Topic:", placeholder="e.g., The Future of Renewable Energy")
    content_goal = st.text_input("Content Goal:", placeholder="e.g., To inform beginners about solar power")
    total_word_count = st.number_input("Target Word Count:", min_value=100, max_value=5000, value=1000, step=100)
    supporting_keywords = st.text_input("Supporting Keywords (comma-separated):", placeholder="e.g., solar panels, wind turbines, sustainability")

# --- Main Content Area ---
st.header("✍️ Your Content")
original_content = st.text_area("Paste your original content here:", height=300, placeholder="Start with a paragraph or even just a few sentences...")

# Generate Content Button
if st.button("✨ Augment Content"):
    # --- Input Validation ---
    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar.")
    elif not primary_topic or not content_goal or not original_content:
        st.warning("Please fill out all the required fields: Primary Topic, Content Goal, and Original Content.")
    else:
        try:
            # --- API Call ---
            with st.spinner("Augmenting your content... Please wait."):
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-2.5-pro') # Or use 'gemini-pro'

                # The detailed custom prompt
                prompt = f"""
# Role: Expert Content Strategist and Editor

## Primary Mission:
Your task is to analyze, expand, and refine a provided piece of content based on specific strategic goals. You will act as an expert writer who can seamlessly mimic any writing style to create a more comprehensive and effective final piece.

## Input Data:
You will be provided with the following five pieces of information:

1.  **`[Primary Topic]`:** {primary_topic}
2.  **`[Content Goal]`:** {content_goal}
3.  **`[Total Word Count]`:** {total_word_count}
4.  **`[Supporting Keywords]`:** {supporting_keywords}
5.  **`[Original Content]`:** {original_content}

## Step-by-Step Instructions:

1.  **Analyze the Foundation:** First, thoroughly read and understand the `[Original Content]`. Pay close attention to its existing tone, voice, sentence structure, and overall writing style. Simultaneously, analyze the specified `[Primary Topic]` and `[Content Goal]`.

2.  **Identify Content Gaps:** Critically evaluate the `[Original Content]` in relation to the `[Primary Topic]` and `[Content Goal]`. Identify any missing information, underdeveloped arguments, unexplored sub-topics, or logical gaps that prevent the content from fully and comprehensively covering the subject matter and achieving its goal.

3.  **Generate and Integrate New Content:** Based on your gap analysis, generate new, high-quality content to fill these voids. The new content you create **MUST** perfectly mimic the tone and style of the `[Original Content]`. You have the creative freedom to insert this new content at the beginning, in the middle, or at the end—wherever it creates the most logical and seamless flow to enhance the overall piece. The transition between original and new text should be undetectable to a reader.

4.  **Incorporate Keywords:** As you integrate the new content, naturally weave the provided `[Supporting Keywords]` throughout the entire text (in both the original and newly generated sections). Avoid "keyword stuffing"; the keywords should feel like a natural part of the prose.

5.  **Adhere to Word Count:** The final, complete output must be approximately the `[Total Word Count]`. Expand upon your newly generated sections or add more detail to existing sentences as needed to reach this target. If the `[Original Content]` is already near the target word count, focus more on refinement and targeted additions rather than extensive expansion.

6.  **Final Output:** Produce **ONLY** the final, complete, and seamlessly integrated version of the content. Do not include any of your own analysis, comments, explanations, or headings like "Revised Content." The output should be a single block of text, ready for immediate use.
"""

                # Generate content
                response = model.generate_content(prompt)
                augmented_content = response.text

                # --- Display Result ---
                st.header("🚀 Augmented Content")
                st.markdown(augmented_content)
                st.success("Content generation complete!")

        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.info("Please check your API key and the model name. Ensure the API key has the correct permissions.")

