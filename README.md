# Emotion Detection AI 😊

A production-ready AI-based emotion detection system with Flask backend and interactive frontend, deployable on Netlify.

## Features

- 🎨 Beautiful, responsive UI
- 📸 Drag-and-drop image upload
- 🤖 Real-time emotion detection using TensorFlow/Keras
- 😊 Support for 7 emotions: Angry, Happy, Sad, Surprise, Neutral, Fear, Disgust
- 📊 Confidence scores for predictions
- 🚀 Production-ready code with error handling
- ☁️ Ready for Netlify deployment

## Tech Stack

### Backend
- **Framework**: Flask
- **Model**: TensorFlow/Keras (emotion_model.h5)
- **Image Processing**: OpenCV
- **Language**: Python

### Frontend
- **Framework**: Vanilla JavaScript (no dependencies)
- **Styling**: CSS3 with animations
- **Build Tool**: None required (static files)

### Deployment
- **Platform**: Netlify
- **Backend Deployment**: Railway, Render, Heroku, or AWS

## Project Structure

```
.
├── index.html              # Main frontend application
├── app.py                  # Flask backend API
├── netlify.toml            # Netlify configuration
├── package.json            # Node dependencies
├── functions/
│   └── predict.js          # Netlify Function (proxy to Flask)
├── emotion_model.h5        # Pre-trained model (place here)
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Setup & Installation

### 1. Local Development

#### Prerequisites
- Python 3.8+
- Node.js 14+
- pip (Python package manager)

#### Install Python Dependencies
```bash
pip install flask numpy opencv-python tensorflow
```

#### Install Node Dependencies
```bash
npm install
```

#### Run Flask Backend (Terminal 1)
```bash
python app.py
```
The backend will run on `http://localhost:5000`

#### Run Frontend Locally (Terminal 2)
```bash
npm run dev
# or
netlify dev
```
The frontend will run on `http://localhost:3000` or `http://localhost:8888`

### 2. Prepare Model
- Ensure you have `emotion_model.h5` in the project root
- The model should accept input shape (1, 48, 48, 1) and output 7 emotion classes

## Deployment Guide

### Option 1: Deploy Everything to Netlify (Recommended)

#### Step 1: Deploy Backend to Railway/Render

**Using Railway:**
1. Go to [railway.app](https://railway.app)
2. Click "New Project" → "Deploy from GitHub"
3. Connect your repository
4. Add environment variables:
   - `FLASK_ENV=production`
5. Railway automatically detects Python and sets up
6. Copy your Railway URL (e.g., `https://myapp-prod-up.railway.app`)

**Using Render:**
1. Go to [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn app:app`
6. Add environment: `Python 3.11`
7. Copy your Render URL

#### Step 2: Deploy Frontend to Netlify

1. Push your code to GitHub:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/emotion-detection.git
git push -u origin main
```

2. Go to [netlify.com](https://netlify.com) and sign in
3. Click "Add new site" → "Import an existing project"
4. Select your GitHub repository
5. Configure:
   - **Build command**: `npm install`
   - **Publish directory**: `.` (root)
6. Set environment variables:
   - `FLASK_API_URL`: your Railway/Render URL (e.g., `https://myapp-prod-up.railway.app`)
7. Deploy!

#### Step 3: Enable CORS on Flask Backend

Update your Flask app to allow Netlify domain:

```python
from flask_cors import CORS

CORS(app, resources={r"/predict": {"origins": ["https://your-netlify-domain.netlify.app"]}})
```

Or install flask-cors:
```bash
pip install flask-cors
```

### Option 2: Deploy Everything to Heroku (Legacy)

```bash
# Install Heroku CLI
# Login
heroku login

# Create app
heroku create emotion-detection-app

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

### Option 3: Deploy to AWS

1. **Backend (EC2)**:
   - Launch EC2 instance
   - Install Python, dependencies
   - Run Flask with Gunicorn
   - Configure security groups

2. **Frontend (S3 + CloudFront)**:
   - Create S3 bucket
   - Upload index.html
   - Create CloudFront distribution
   - Update API endpoint to EC2 URL

## API Endpoints

### Backend (Flask)

**Predict Endpoint**
```
POST /predict
Content-Type: multipart/form-data

Parameters:
- image: (binary) Image file (PNG, JPG, GIF, BMP)

Response:
{
  "emotion": "Happy",
  "confidence": 0.9845
}
```

**Health Check**
```
GET /health

Response:
{
  "status": "healthy",
  "model_status": "loaded",
  "emotions": ["Angry", "Happy", "Sad", "Surprise", "Neutral", "Fear", "Disgust"]
}
```

## Environment Variables

### Backend (Flask)
- `FLASK_ENV`: Set to `production` for production
- `FLASK_DEBUG`: Set to `0` for production

### Frontend (Netlify)
- `FLASK_API_URL`: URL of Flask backend API

## Performance Optimization

### Frontend
- Lazy loading for images
- CSS animations for smooth UX
- Responsive design for mobile

### Backend
- Model caching (loaded once on startup)
- Image preprocessing optimization
- Error logging for debugging

## Troubleshooting

### Model not loading
```
Error: Failed to load model
```
**Solution**: Ensure `emotion_model.h5` is in the same directory as `app.py`

### CORS errors
```
Error: Cross-Origin Request Blocked
```
**Solution**: 
- Add `flask-cors` to your backend
- Set correct `FLASK_API_URL` in Netlify environment variables

### Image upload fails
```
Error: Failed to process image file
```
**Solution**:
- Use supported formats: PNG, JPG, GIF, BMP
- Keep file size under 10MB
- Ensure image contains detectable face

### Backend connection timeout
```
Error: Failed to connect to Flask backend
```
**Solution**:
- Verify backend is running and accessible
- Check firewall/security group settings
- Ensure `FLASK_API_URL` is correct

## Development Tips

### Testing Locally
```bash
# Terminal 1: Start Flask
python app.py

# Terminal 2: Start Netlify dev server
netlify dev

# Open browser
http://localhost:3000
```

### Testing with cURL
```bash
curl -X POST \
  -F "image=@test_image.jpg" \
  http://localhost:5000/predict
```

### Enable Debug Logging
In `app.py`, set:
```python
logging.basicConfig(level=logging.DEBUG)
```

## Production Checklist

- [ ] Model file (`emotion_model.h5`) uploaded
- [ ] Flask backend deployed to Railway/Render
- [ ] CORS configured properly
- [ ] Environment variables set on Netlify
- [ ] Frontend deployed to Netlify
- [ ] Test emotion detection with sample images
- [ ] Monitor backend logs for errors
- [ ] Set up domain name (optional)
- [ ] Enable HTTPS (automatic on Netlify)

## Next Steps

1. **Add Model Training**: Create your own emotion detection model
2. **Add Database**: Store prediction history
3. **Add Authentication**: User accounts and API keys
4. **Add Analytics**: Track emotions over time
5. **Mobile App**: React Native version
6. **Advanced Features**: Live camera feed, batch predictions

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [TensorFlow/Keras Models](https://www.tensorflow.org/guide/keras)
- [Netlify Documentation](https://docs.netlify.com/)
- [Railway Deployment Guide](https://docs.railway.app/)
- [OpenCV Tutorial](https://docs.opencv.org/)

## License

MIT License - feel free to use for personal or commercial projects

## Support

For issues or questions, please open an issue or contact support.

---

**Happy Detecting! 😊**
