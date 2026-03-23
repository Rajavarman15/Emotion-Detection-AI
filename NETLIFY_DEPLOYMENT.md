# Quick Netlify Deployment Guide

This guide will help you deploy the Emotion Detection AI application to Netlify in 5 minutes.

## Step 1: Prepare Your Repository

1. Initialize Git (if not already done):
```bash
git init
git add .
git commit -m "Initial emotion detection app"
```

2. Create a new repository on [GitHub](https://github.com/new)

3. Push your code:
```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/emotion-detection.git
git push -u origin main
```

## Step 2: Deploy Backend (Choose One)

### Option A: Railway (Recommended - Easiest)

1. Go to [railway.app](https://railway.app)
2. Click "New Project" 
3. Select "Deploy from GitHub"
4. Authorize and select your repository
5. Railroad will auto-detect it's a Python project
6. Wait for deployment (2-3 minutes)
7. Go to "Settings" → "Domains"
8. Copy your Railway URL (e.g., `https://myapp-prod-up.railway.app`)

### Option B: Render

1. Go to [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect GitHub repository
4. Fill settings:
   - **Name**: emotion-detection
   - **Environment**: Python 3
   - **Build command**: `pip install -r requirements.txt`
   - **Start command**: `gunicorn app:app`
5. Click "Create Web Service"
6. Copy your Render URL after deployment (e.g., `https://emotion-detection.onrender.com`)

### Option C: Heroku (Free tier retired, paid only)

```bash
heroku login
heroku create emotion-detection-app
git push heroku main
heroku open
```

## Step 3: Deploy Frontend to Netlify

1. Go to [netlify.com](https://netlify.com)
2. Sign up / Log in with GitHub
3. Click "Add new site"
4. Select "Import an existing project"
5. Choose your GitHub repository
6. Configure Build Settings:
   - **Base directory**: (leave empty)
   - **Build command**: `npm install` (or leave empty if no build needed)
   - **Publish directory**: `.` (root folder)

7. Click "Deploy site"
8. Wait for deployment (1-2 minutes)
9. Copy your Netlify URL (e.g., `https://emotion-detection-app.netlify.app`)

## Step 4: Configure Environment Variables

1. In Netlify Dashboard, go to your site
2. Click "Site settings" → "Build & deploy" → "Environment"
3. Click "Edit variables"
4. Add new variable:
   - **Key**: `FLASK_API_URL`
   - **Value**: Your Railway/Render URL (e.g., `https://emotion-detection-prod.railway.app`)
5. Click "Save"
6. Go to "Deployments" and click "Trigger deploy" to redeploy with new variables

## Step 5: Test Your Deployment

1. Open your Netlify URL in browser
2. Click "Predict Emotion" button
3. Upload a test image
4. See the emotion detection result!

## Troubleshooting

### Frontend deployed but shows error

**Problem**: `Failed to connect to Flask backend`

**Solutions**:
1. Verify backend is deployed and accessible:
   ```bash
   curl https://your-railway-url/health
   ```
2. Check `FLASK_API_URL` environment variable is set correctly
3. Redeploy frontend after setting environment variable
4. Check CORS is enabled in Flask app (included in provided `app.py`)

### Backend deployment failed

**Problem**: Build fails on Railway/Render

**Solutions**:
1. Ensure `requirements.txt` has all dependencies
2. Check Python version compatibility 
3. Verify `emotion_model.h5` is in the repository
4. Check build logs for specific errors

### Image upload not working

**Problem**: Cannot upload images locally

**Solutions**:
1. Ensure Flask backend is running (`python app.py`)
2. Check browser console for CORS errors
3. Use supported formats: PNG, JPG, GIF, BMP

## Deployment Checklist

- [ ] Repository pushed to GitHub
- [ ] Backend deployed to Railway/Render
- [ ] Backend URL copied
- [ ] Frontend deployed to Netlify  
- [ ] Environment variables set in Netlify
- [ ] Frontend redeployed after setting variables
- [ ] Test with sample image works
- [ ] Emotions are detected correctly

## Cost

- **Frontend (Netlify)**: FREE
- **Backend (Railway)**: FREE tier available (~$5/month if upgraded)
- **Backend (Render)**: FREE tier available
- **Total**: Can be completely FREE!

## Next Steps

1. Share your Netlify URL with friends
2. Add custom domain (optional)
3. Monitor predictions and model accuracy
4. Consider training your own emotion model
5. Add features like emotion history, batch processing, etc.

## Support

- [Netlify Docs](https://docs.netlify.com/)
- [Railway Docs](https://docs.railway.app/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [GitHub Issues](https://github.com/yourusername/emotion-detection/issues)

---

**Your app is live! 🎉**

Share your Netlify URL and start detecting emotions!
