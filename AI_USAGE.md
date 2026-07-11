# AI_USAGE.md

This file documents how AI tools were used during development, and how
the core content-generation prompt was iterated and improved.

## AI Tools Used
- **Claude** — used for ideation, code scaffolding help, and debugging
  the Streamlit + Grok API integration.
- **Grok API (`grok-4`)** — the model powering the actual content
  generation feature inside the app itself.

## How AI Was Used in Development
- Brainstormed the template structure (which content types + which
  controls make sense together).
- Got help structuring the Streamlit layout (sidebar for inputs, main
  area for output + prompt transparency panel).
- Used AI to debug the Grok API request/response format.
- Wrote first-draft README and documentation sections, then edited for
  accuracy to match the actual code.

All logic was reviewed and understood before inclusion — nothing was
copy-pasted blindly.

## Prompt Strategy Notes

The app uses a **two-part prompt structure** for every generation:
1. **System prompt** — defines the *persona* for that content type (e.g.
   "You are an e-commerce copywriter...") so tone/style stays consistent
   per template.
2. **User prompt** — built dynamically from the form inputs (topic,
   keywords, tone, length, audience, format).

### Prompt Improvement Iterations

**Iteration 1 (initial, too vague):**
```
Write a blog post about {topic}.
```
Problem: Output length and structure were inconsistent, no control over
tone, sometimes included unwanted preamble like "Sure, here's a blog post...".

**Iteration 2 (added constraints):**
```
Write a blog post about {topic} in a {tone} tone. Keep it {length}.
```
Problem: Better, but still occasionally added an intro sentence like
"Here is your blog post:" before the actual content, and ignored the
target audience.

**Iteration 3 (final — used in app):**
```
Write a blog post about: {topic}

Target audience: {audience}
Tone: {tone}
Length: {length_desc}
Keywords/points to include (if relevant): {keywords}

{format_instruction}
Return only the final content, no explanations or preamble.
```
Result: Explicit structure + an instruction to skip preamble reliably
removed the "Sure, here's..." wrapper text and made output length and
audience targeting far more consistent across all 6 templates.

### Key Lessons
- Explicitly telling the model to return "only the final content" was
  the single biggest fix for clean, copy-paste-ready output.
- Separating persona (system prompt) from task details (user prompt)
  made it easy to reuse one prompt-builder function across all 6
  templates instead of writing six different prompt functions.
- Giving a concrete word-count description (e.g. "around 150-250 words")
  worked better than vague labels like "medium length" alone.
