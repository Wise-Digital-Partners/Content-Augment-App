Content Augmentation App with Gemini & Streamlit
================================================

This Streamlit application leverages the power of the Google Gemini API to analyze, expand, and refine user-provided content based on specific strategic goals. It acts as an expert content strategist, seamlessly integrating new information while mimicking the original writing style.

🚀 How to Run Locally
---------------------

1.  **Clone the Repository:**

    ```
    git clone <your-repo-url>
    cd <your-repo-name>

    ```

2.  **Create a Virtual Environment (Recommended):**

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    ```

3.  **Install Dependencies:**

    ```
    pip install -r requirements.txt

    ```

4.  **Get Your Gemini API Key:**

    -   Go to [Google AI Studio](https://makersuite.google.com/app/apikey "null").

    -   Create a new API key.

    -   Copy the key.

5.  **Run the Streamlit App:**

    ```
    streamlit run app.py

    ```

    The application will open in your web browser. Paste your API key into the input field in the sidebar to get started.

☁️ How to Deploy on Streamlit Community Cloud
---------------------------------------------

Deploying this app is free and straightforward.

1.  **Push to GitHub:**

    -   Create a new repository on GitHub.

    -   Add your files (`app.py`, `requirements.txt`, `README.md`) to the repository.

    -   Commit and push your changes:

        ```
        git init
        git add .
        git commit -m "Initial commit"
        git branch -M main
        git remote add origin [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
        git push -u origin main

        ```

2.  **Deploy on Streamlit:**

    -   Go to [share.streamlit.io](https://share.streamlit.io/ "null").

    -   Click "**New app**".

    -   Connect your GitHub account.

    -   Select your repository and the `main` branch. The main script path should be `app.py`.

    -   Click "**Advanced settings**" and go to the "**Secrets**" section. This is crucial for keeping your API key secure.

    -   Add your Gemini API key as a secret. The format should be:

        ```
        GEMINI_API_KEY="your-actual-api-key-goes-here"

        ```

    -   Click "**Deploy!**" Streamlit will handle the rest. Your app will be live in a few minutes.

✨ Features
----------

-   **Intuitive UI:** A clean interface built with Streamlit for entering content and strategic goals.

-   **Powerful Augmentation:** Uses the Gemini 2.5 Pro model to perform a deep analysis and generate high-quality, context-aware content.

-   **Style Mimicking:** Seamlessly matches the tone and voice of your original content.

-   **Keyword Integration:** Naturally weaves in supporting keywords to improve SEO.

-   **Word Count Control:** Aims for a specific target word count for the final piece.

-   **Secure API Key Handling:** Uses Streamlit Secrets for safe API key management in deployed apps.
