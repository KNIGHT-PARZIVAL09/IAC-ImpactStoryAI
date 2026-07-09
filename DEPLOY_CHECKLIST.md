# ✅ Quick Deployment Checklist

## 🚀 Deploy to Streamlit Cloud in 10 Minutes

### Step 1: Create GitHub Account (if you don't have one)
- [ ] Go to https://github.com/signup
- [ ] Create free account

### Step 2: Create Repository
- [ ] Go to https://github.com/new
- [ ] Name: `IAC-ImpactStoryAI`
- [ ] Set to **Public**
- [ ] Click "Create repository"

### Step 3: Upload Files
- [ ] Click "uploading an existing file" on GitHub
- [ ] Drag ALL files from `ImpactStoryAI` folder
- [ ] **EXCEPT**: Do NOT upload `.env` file
- [ ] Commit changes

### Step 4: Deploy on Streamlit
- [ ] Go to https://share.streamlit.io/
- [ ] Click "New app"
- [ ] Connect GitHub
- [ ] Select your repository
- [ ] Main file: `app.py`

### Step 5: Add Secret
- [ ] Click "Advanced settings"
- [ ] In Secrets section, paste:
```
GEMINI_API_KEY = "your_actual_gemini_api_key_here"
```
- [ ] Replace with your real API key from `.env` file

### Step 6: Deploy!
- [ ] Click "Deploy"
- [ ] Wait 2-5 minutes
- [ ] Get your URL!

---

## 🎯 Your Current Setup

**API Key**: Check your `.env` file
**Model**: `models/gemini-2.5-flash`
**Files to Upload**: Everything EXCEPT `.env`

---

## 🔗 Important Links

- **Create GitHub Repo**: https://github.com/new
- **Deploy App**: https://share.streamlit.io/
- **Get API Key**: https://makersuite.google.com/app/apikey

---

## 📋 Files You Have

Your `ImpactStoryAI` folder contains:
```
✅ app.py (main application)
✅ requirements.txt (dependencies)
✅ utils/ folder (helper functions)
✅ .gitignore (security)
✅ .streamlit/config.toml (theme)
✅ README.md (documentation)
❌ .env (DO NOT UPLOAD - contains secret key)
```

---

## 🎉 After Deployment

You'll get a URL like:
```
https://your-app-name.streamlit.app
```

**Share this URL with anyone!** The app is now live! 🚀

---

## ⚡ Quick Commands (if using Git CLI)

```bash
cd ImpactStoryAI
git init
git add .
git commit -m "Initial deployment"
git remote add origin https://github.com/YourUsername/IAC-ImpactStoryAI.git
git push -u origin main
```

Then deploy on Streamlit Cloud as described above.

---

**Need Help?** Check `DEPLOYMENT_GUIDE.md` for detailed instructions! 📚✨
