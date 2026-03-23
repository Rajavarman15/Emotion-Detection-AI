# 🚀 Deploy to Netlify - Step by Step

Your Emotion Detection AI is ready to go live! Follow these steps to deploy like https://dlssabad106.netlify.app/

---

## 📋 CHECKLIST

### Phase 1: GitHub Setup (5-10 minutes)

- [ ] Open Command Prompt in `d:\dl ssa`
- [ ] Run `setup-github.bat`
- [ ] Go to https://github.com/new (create new repository)
- [ ] Name it: `emotion-detection` (or your preferred name)
- [ ] Copy the GitHub URL from quick setup (looks like: `https://github.com/yourusername/emotion-detection.git`)
- [ ] Run the git push commands shown in setup

**Commands to run after setup-github.bat:**
```powershell
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/emotion-detection.git
git push -u origin main
```

### Phase 2: Deploy Backend to Railway (3-5 minutes)

- [ ] Go to https://railway.app
- [ ] Sign up with GitHub (click "Deploy from GitHub")
- [ ] Authorize Railway to access your GitHub
- [ ] Find your `emotion-detection` repository and click it
- [ ] Railway auto-detects Python project
- [ ] Wait ~2-3 minutes for deployment
- [ ] Go to "Settings" → "Domains"
- [ ] **Copy the domain URL** (looks like: `https://emotion-detection-prod.railway.app`)
- [ ] Save this URL for next step!

**⚠️ IMPORTANT: Save your Railway URL before moving to Phase 3**

### Phase 3: Deploy Frontend to Netlify (3-5 minutes)

- [ ] Go to https://netlify.com
- [ ] Click "Sign up" → Select "GitHub"
- [ ] Authorize Netlify to access your GitHub
- [ ] Click "Add new site" → "Import an existing project"
- [ ] Select your `emotion-detection` repository
- [ ] Configure deployment:
  - **Base directory**: (leave empty)
  - **Build command**: `npm install`
  - **Publish directory**: `.` (the root)
- [ ] Click "Deploy site"
- [ ] Wait for deployment (1-2 minutes)
- [ ] Your site URL appears (looks like: `https://emotion-detection-xx.netlify.app`)
- [ ] **Copy this Netlify URL**

### Phase 4: Connect Frontend to Backend (2 minutes)

**Back in Netlify Dashboard:**

- [ ] Click your site name
- [ ] Go to "Site settings" → "Build & deploy" → "Environment"
- [ ] Click "Edit variables"
- [ ] Add environment variable:
  - **Key**: `FLASK_API_URL`
  - **Value**: (Paste your Railway URL from Phase 2)
  - Example: `https://emotion-detection-prod.railway.app`
- [ ] Click "Save"
- [ ] Go to "Deployments"
- [ ] Find the latest deployment and click the menu (⋯)
- [ ] Click "Trigger deploy"
- [ ] Wait for new deployment with environment variables

### Phase 5: Test Live Deployment (2-3 minutes)

- [ ] Open your Netlify URL in browser
- [ ] Try uploading an image
- [ ] Click "Predict Emotion"
- [ ] **You should see emotion detection results!**

---

## 🎯 Expected Results

**If it works:**
- ✅ Frontend loads beautiful UI
- ✅ Can upload images by dragging
- ✅ Predictions return with emotion names
- ✅ Confidence scores display
- ✅ No CORS errors in browser console

**If you see errors:**

| Error | Solution |
|-------|----------|
| `CORS errors` | Environment variable not set. Re-deploy Phase 4. |
| `Cannot reach backend` | Railway URL incorrect. Check Phase 2 URL is right. |
| `Page not found (404)` | Netlify build failed. Check deploy logs. |
| `Blank page` | Check browser console for JavaScript errors. |

---

## 💡 Helpful Tips

### Find Your URLs

**Netlify URL** - In Netlify Dashboard:
- Click your site → Copy "Site URL" at top

**Railway URL** - In Railway Dashboard:
- Click your project → Go to "Settings" → "Domains" → Copy domain

### Check Deployment Logs

**Netlify**: Dashboard → Deployments → Click deployment → View logs
**Railway**: Dashboard → Project → Logs tab

### Verify Backend is Running

Open this in browser:
```
https://your-railway-url/health
```

You should see:
```json
{
  "status": "healthy",
  "model_status": "...",
  "emotions": ["Angry", "Happy", ...]
}
```

---

## 🔄 Update Your App

Once deployed, if you make changes:

1. **Make changes** to your code
2. **Commit and push** to GitHub:
   ```bash
   git add .
   git commit -m "Your update message"
   git push origin main
   ```
3. **Automatic redeploy**: Netlify & Railway auto-redeploy from GitHub!

---

## 🎉 You're Done!

Share your live URL with friends! Your app is now live on the internet.

Example final URL: `https://emotion-detection-abc123.netlify.app`

---

## 📞 Troubleshooting

### Backend won't deploy on Railway
- Ensure `requirements.txt` has all packages
- Check build logs for errors
- Verify `app.py` runs locally first

### Frontend blank/errors on Netlify
- Check browser console (F12 → Console tab)
- Verify `FLASK_API_URL` environment variable is set
- Trigger a new deploy after setting variable

### Emotion predictions all same emotion
- If using test mode, predictions are random
- When real model is ready, replace `emotion_model.h5`
- Restart backend with new model

### Connection timeout errors
- Railway instance might be sleeping (free tier)
- Make a request to wake it up
- Or upgrade to paid tier

---

## 🚀 Advanced: Using Your Own Model

When you have a real trained `emotion_model.h5`:

1. Replace the test model file
2. Test locally: `python app.py`
3. Commit and push to GitHub
4. Railway auto-redeploys with new model
5. Predictions become accurate!

---

**Ready? Follow the checklists above!** 🚀
