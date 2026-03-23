# Clean Restart: Simple Deploy Plan

## Goal: Deploy emotion AI as live link (Netlify/GitHub Pages)

**Step 1: Skip model – use test mode**
```cmd
python app.py
```
(Server starts localhost:5000)

**Step 2: ngrok tunnel**
```cmd
./ngrok.exe http 5000
```
(Copy public URL)

**Step 3: Manual Netlify deploy**
- netlify.com > Drag folder
- Env var: FLASK_API_URL = ngrok URL
- Live *.netlify.app link

**Local test**: Open index.html

**Current: Clean slate – run Step 1**
