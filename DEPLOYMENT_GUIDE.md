# 🚀 Complete Deployment Guide

## Option 1: Streamlit Community Cloud (Recommended - FREE)

### Prerequisites
- GitHub account (create at https://github.com)
- Your Gemini API key

### Step 1: Create GitHub Repository

1. **Go to GitHub**: https://github.com/new
2. **Repository name**: `IAC-ImpactStoryAI`
3. **Description**: `AI-powered storytelling app for IAC participants`
4. **Make it Public** (required for free Streamlit Cloud)
5. Click **"Create repository"**

### Step 2: Upload Your Code to GitHub

**Option A: Using GitHub Web Interface (Easiest)**

1. On your new repository page, click **"uploading an existing file"**
2. **Drag and drop ALL files** from your `ImpactStoryAI` folder
   - ✅ Include: `app.py`, `utils/`, `requirements.txt`, `.gitignore`, etc.
   - ❌ Exclude: `.env` file (important!)
3. Write commit message: "Initial commit - Impact Story AI"
4. Click **"Commit changes"**

**Option B: Using GitHub Desktop (If you have it)**

1. Download GitHub Desktop: https://desktop.github.com/
2. Open GitHub Desktop
3. File → Add Local Repository → Select `ImpactStoryAI` folder
4. Click "Publish repository"

### Step 3: Deploy on Streamlit Cloud

1. **Go to**: https://share.streamlit.io/
2. Click **"New app"**
3. **Connect to GitHub** (authorize Streamlit)
4. Select:
   - **Repository**: `YourUsername/IAC-ImpactStoryAI`
   - **Branch**: `main` (or `master`)
   - **Main file path**: `app.py`
5. Click **"Advanced settings"**

### Step 4: Add Your API Key as Secret

In the Advanced settings:

1. Under **"Secrets"**, add:

```toml
GEMINI_API_KEY = "your_actual_gemini_api_key_here"
```

2. Click **"Deploy!"**

### Step 5: Wait for Deployment

- Takes 2-5 minutes
- You'll see build logs
- When done, you'll get a URL like: `https://iac-impactstoryai.streamlit.app`

### 🎉 That's it! Your app is live!

---

## Option 2: Heroku (Paid)

### Prerequisites
- Heroku account: https://heroku.com
- Heroku CLI installed

### Files Needed

Create `Procfile`:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

Create `runtime.txt`:
```
python-3.11.0
```

### Deploy Commands

```bash
heroku login
heroku create iac-impact-story
heroku config:set GEMINI_API_KEY=your_api_key_here
git init
git add .
git commit -m "Initial commit"
git push heroku main
```

---

## Option 3: AWS/Azure/GCP

See DEPLOYMENT.md for detailed cloud platform instructions.

---

## 🔒 Security Checklist

Before deploying:

- [ ] ✅ `.env` file is in `.gitignore`
- [ ] ✅ No API keys in code
- [ ] ✅ API key added as secret in Streamlit Cloud
- [ ] ✅ `.gitignore` includes sensitive files

---

## 📝 Post-Deployment

### Update Your App

1. Make changes locally
2. Upload to GitHub (or push with Git)
3. Streamlit Cloud auto-deploys in 1-2 minutes

### Monitor Your App

- View logs in Streamlit Cloud dashboard
- Check usage/analytics
- Monitor API quota

### Custom Domain (Optional)

In Streamlit Cloud settings:
- Add custom domain
- Update DNS records
- Enable HTTPS (automatic)

---

## 🐛 Troubleshooting

### App Won't Start

- Check build logs in Streamlit Cloud
- Verify all files uploaded to GitHub
- Check requirements.txt has correct packages

### API Key Error

- Verify secret is added in Streamlit Cloud
- Check secret format (no extra quotes)
- Regenerate API key if needed

### Import Errors

- Ensure all files in `utils/` folder uploaded
- Check `requirements.txt` has all dependencies

---

## 🎯 Your Deployment Checklist

### Before Deployment
- [ ] Test app locally (works perfectly)
- [ ] Create GitHub repository
- [ ] Upload all files to GitHub (except .env)
- [ ] Verify .gitignore is working

### During Deployment
- [ ] Sign up for Streamlit Cloud
- [ ] Connect GitHub repository
- [ ] Add API key as secret
- [ ] Deploy app

### After Deployment
- [ ] Test live app
- [ ] Check all features work
- [ ] Share URL with team
- [ ] Set up monitoring

---

## 📱 Your Live App URL

After deployment, you'll get a URL like:
```
https://iac-impactstoryai.streamlit.app
```

Share this with anyone! It's public and ready to use. 🎉

---

## 💡 Pro Tips

1. **Free Tier Limits**: Streamlit Cloud free tier:
   - 1GB RAM
   - 1 CPU core
   - Public repositories only
   - Multiple apps allowed

2. **Performance**: For better performance, consider:
   - Streamlit Cloud paid tier ($20/mo)
   - Heroku Standard ($25/mo)
   - AWS/GCP (custom pricing)

3. **Monitoring**: Set up:
   - Google Analytics (optional)
   - Error tracking (Sentry)
   - Usage logs

---

**Need help? Check the full guide or contact support!** 🚀✨
