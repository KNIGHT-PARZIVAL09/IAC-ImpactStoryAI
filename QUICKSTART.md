# 🚀 Quick Start Guide

Get your AI Storytelling application running in 5 minutes!

## Step 1: Install Dependencies

```bash
cd ImpactStoryAI
pip install -r requirements.txt
```

## Step 2: Get Your Gemini API Key

1. Go to https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key

## Step 3: Configure API Key

Open `.env` file and add your key:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

## Step 4: Run the Application

```bash
streamlit run app.py
```

## Step 5: Use the Application

1. **Paste your content** in the three text areas:
   - LinkedIn posts
   - Internship reviews
   - Training reviews

2. **Select settings**:
   - Choose Tone (Professional/Inspirational/LinkedIn Ready)
   - Choose Length (Short/Medium/Long)

3. **Generate** your story by clicking "🚀 Generate Story"

4. **Export** as DOCX or PDF

That's it! 🎉

---

## Troubleshooting

**Issue**: Module not found error  
**Fix**: `pip install -r requirements.txt`

**Issue**: API key error  
**Fix**: Check your `.env` file has the correct key without quotes

**Issue**: Port in use  
**Fix**: `streamlit run app.py --server.port 8502`

---

For detailed documentation, see [README.md](README.md)
