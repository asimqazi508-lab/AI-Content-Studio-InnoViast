import streamlit as st
from groq import Groq

# ── Page Config ──────────────────────────────────────────────
st.set_page_config(
    page_title="AI Content Studio",
    page_icon="✍️",
    layout="wide"
)

# ── Groq Client ───────────────────────────────────────────────
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
# ── Custom CSS ────────────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #0f1117; }
    .stButton>button {
        background: linear-gradient(135deg, #6c63ff, #a78bfa);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 24px;
        font-size: 16px;
        width: 100%;
    }
    .stButton>button:hover { opacity: 0.9; }
    .output-box {
        background: #1e2434;
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 12px;
        padding: 20px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────
st.title("✍️ AI Content Generation Studio")
st.markdown("Generate high-quality content in seconds!")
st.divider()

# ── Sidebar Controls ──────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Content Settings")

    template = st.selectbox("📄 Content Type", [
        "Blog Post",
        "Instagram Caption",
        "Ad Copy",
        "Email",
        "Product Description",
        "LinkedIn Post"
    ])

    tone = st.selectbox("🎭 Tone", [
        "Professional",
        "Casual",
        "Funny",
        "Inspirational",
        "Formal"
    ])

    audience = st.selectbox("👥 Target Audience", [
        "General Public",
        "Students",
        "Business Professionals",
        "Teenagers",
        "Entrepreneurs"
    ])

    length = st.selectbox("📏 Length", [
        "Short (50-100 words)",
        "Medium (150-250 words)",
        "Long (300-500 words)"
    ])

# ── Main Input ────────────────────────────────────────────────
topic = st.text_area(
    "💡 What do you want to write about?",
    placeholder="E.g. Benefits of drinking water daily...",
    height=120
)

# ── Generate Button ───────────────────────────────────────────
if st.button("🚀 Generate Content"):
    if not topic.strip():
        st.warning("Please enter a topic first!")
    else:
        with st.spinner("Generating your content..."):

            prompt = f"""You are an expert content writer.
            
Write a {template} about: {topic}

Settings:
- Tone: {tone}
- Target Audience: {audience}  
- Length: {length}

Write only the content, no extra explanation."""

            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=800,
                    temperature=0.8,
                )
                result = response.choices[0].message.content

                st.success("✅ Content Generated!")
                st.markdown("### 📋 Your Content:")
                st.markdown(f'<div class="output-box">{result}</div>', unsafe_allow_html=True)

                # Copy button
                st.code(result, language="")

            except Exception as e:
                st.error("⚠️ Something went wrong. Please try again!")