# AI Content Generation Studio — InnoViast

**Track:** 03 - AI Solutions Engineering
**Week 2 — Assignment 2:** AI Content Generation Studio

## Overview
A Streamlit-based content writing assistant that generates high-quality,
structured content for multiple real-world use cases: blog posts, social
captions, ad copy, emails, product descriptions, and LinkedIn posts. Users
control tone, length, target audience, and output format, then edit and
export the generated content.

## Problem Statement
Creating varied, on-brand marketing/content copy manually is slow and
inconsistent. This tool lets a user pick a content type, describe the
topic, and instantly get a structured, editable draft — cutting content
creation time significantly.

## Features
- 6 content templates: Blog Post, Social Media Caption, Ad Copy, Email,
  Product Description, LinkedIn Post
- Controls for **Tone**, **Length**, **Target Audience**, **Output Format**
- Editable output box (not just a static result)
- Download generated content as `.md` or `.txt`
- Prompt transparency panel — shows the exact prompt sent to the model
- Generation history for the current session

## Tech Stack
- **Frontend/App:** Streamlit (Python)
- **AI Model:** Grok API (`grok-4`) via x.ai's OpenAI-compatible endpoint
- **Libraries:** `requests`, `python-dotenv`

## Setup Steps
1. Clone the repo:
   ```
   git clone <your-repo-url>
   cd AIContentStudio-InnoViast
   ```
2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create a `.env` file (copy from `.env.example`) and add your key:
   ```
   GROK_API_KEY=your_actual_key_here
   ```
5. Run the app:
   ```
   streamlit run app.py
   ```

## Deployment
Deployed on Streamlit Community Cloud: **[add your live link here]**

> When deploying, add `GROK_API_KEY` under the app's **Secrets** settings
> instead of committing a `.env` file.

## Screenshots
_Add 3-5 screenshots here after building/running the app, e.g.:_
- Main input form
- Generated blog post example
- Generated LinkedIn post example
- Editable output + download buttons

## Learning Outcomes
- Practiced prompt engineering with system + user prompt separation
- Learned to design a reusable template library for multiple content types
- Handled API errors and edge cases gracefully in a Streamlit app
- Practiced clean project structure and environment variable management
  for API key security
