import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="AI Content Studio",
    page_icon="✍️",
    layout="wide"
)

import os
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    .stApp { background: #0a0e1a; }
    
    section[data-testid="stSidebar"] {
        background: #111827 !important;
        border-right: 1px solid #1f2937;
    }
    
    section[data-testid="stSidebar"] * { color: #e5e7eb !important; }
    
    .hero {
        background: linear-gradient(135deg, #1e1b4b 0%, #111827 50%, #0f172a 100%);
        border: 1px solid #312e81;
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        margin-bottom: 30px;
    }
    .hero h1 {
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(135deg, #a78bfa, #6366f1, #38bdf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }
    .hero p {
        color: #94a3b8;
        font-size: 1.1rem;
        margin-top: 10px;
    }
    
    .stat-card {
        background: #111827;
        border: 1px solid #1f2937;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }
    .stat-card .number {
        font-size: 1.8rem;
        font-weight: 700;
        color: #a78bfa;
    }
    .stat-card .label {
        color: #6b7280;
        font-size: 0.85rem;
        margin-top: 4px;
    }
    
    .output-card {
        background: #111827;
        border: 1px solid #312e81;
        border-radius: 16px;
        padding: 28px;
        margin-top: 24px;
        color: #e5e7eb;
        line-height: 1.8;
        font-size: 1rem;
        white-space: pre-wrap;
    }
    
    .badge {
        display: inline-block;
        background: #1e1b4b;
        color: #a78bfa;
        border: 1px solid #4338ca;
        border-radius: 20px;
        padding: 4px 14px;
        font-size: 0.8rem;
        margin: 4px;
    }
    
    .section-title {
        color: #e5e7eb;
        font-size: 1rem;
        font-weight: 600;
        margin-bottom: 8px;
        margin-top: 20px;
    }

    div[data-testid="stSelectbox"] > div {
        background: #1f2937 !important;
        border: 1px solid #374151 !important;
        border-radius: 10px !important;
        color: #e5e7eb !important;
    }

    div[data-testid="stTextArea"] textarea {
        background: #1f2937 !important;
        border: 1px solid #374151 !important;
        border-radius: 12px !important;
        color: #e5e7eb !important;
        font-size: 1rem !important;
    }

    .stButton > button {
        background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 28px !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        width: 100% !important;
        transition: opacity 0.2s !important;
    }
    .stButton > button:hover { opacity: 0.85 !important; }
    
    .stAlert { border-radius: 12px !important; }
    
    footer { visibility: hidden; }
    #MainMenu { visibility: hidden; }
    header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ✍️ AI Content Studio")
    st.markdown("---")
    st.markdown("### ⚙️ Settings")

    template = st.selectbox("Content Type", [
        "📝 Blog Post",
        "📸 Instagram Caption",
        "📢 Ad Copy",
        "📧 Email",
        "🛍️ Product Description",
        "💼 LinkedIn Post"
    ])

    tone = st.selectbox("Tone", [
        "Professional",
        "Casual",
        "Funny",
        "Inspirational",
        "Formal"
    ])

    audience = st.selectbox("Target Audience", [
        "General Public",
        "Students",
        "Business Professionals",
        "Teenagers",
        "Entrepreneurs"
    ])

    length = st.selectbox("Length", [
        "Short (50-100 words)",
        "Medium (150-250 words)",
        "Long (300-500 words)"
    ])

    st.markdown("---")
    st.markdown('<div style="color:#6b7280;font-size:0.8rem">Powered by Groq + LLaMA 3.3</div>', unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>✍️ AI Content Studio</h1>
    <p>Generate professional content in seconds — blogs, captions, emails & more</p>
</div>
""", unsafe_allow_html=True)

# ── Stats ─────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown('<div class="stat-card"><div class="number">6</div><div class="label">Content Types</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="stat-card"><div class="number">5</div><div class="label">Tone Options</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="stat-card"><div class="number">5</div><div class="label">Audiences</div></div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="stat-card"><div class="number">⚡</div><div class="label">Instant Output</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Input ─────────────────────────────────────────────────────
st.markdown('<div class="section-title">💡 What do you want to write about?</div>', unsafe_allow_html=True)
topic = st.text_area("", placeholder="E.g. Benefits of drinking water daily, New product launch, Summer sale promotion...", height=130, label_visibility="collapsed")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    generate = st.button("🚀 Generate Content")

# ── Generate ──────────────────────────────────────────────────
if generate:
    if not topic.strip():
        st.warning("⚠️ Please enter a topic first!")
    else:
        with st.spinner("✨ Crafting your content..."):
            clean_template = template.split(" ", 1)[1] if " " in template else template

            prompt = f"""You are an expert content writer and copywriter.

Write a {clean_template} about: {topic}

Requirements:
- Tone: {tone}
- Target Audience: {audience}
- Length: {length}

Write only the final content. No explanations, no labels, no preamble."""

            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=800,
                    temperature=0.8,
                )
                result = response.choices[0].message.content

                st.markdown("<br>", unsafe_allow_html=True)
                
                # Badges
                st.markdown(f"""
                <div>
                    <span class="badge">📄 {clean_template}</span>
                    <span class="badge">🎭 {tone}</span>
                    <span class="badge">👥 {audience}</span>
                    <span class="badge">📏 {length}</span>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f'<div class="output-card">{result}</div>', unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)
                st.code(result, language="")
                st.caption("👆 Click to copy")

            except Exception as e:
                st.error("⚠️ Something went wrong. Please try again!")