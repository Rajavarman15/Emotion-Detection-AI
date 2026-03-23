# Ultra-Simple Emotion Detection Deploy (ngrok + Netlify)
## Status: Progress ✓ Venv created, deps installing...

### 1. Create Mock Model [Pending - deps installing] 
```bash
# After deps: python create_test_model.py
```
Expected: emotion_model.h5 (optional - test mode works)

### 2. Test Local Backend [Next] 
powershell -Command ".venv/Scripts/Activate.ps1; python test_local.py"

### 3. Start Backend Server ✓ Running
(TF loaded, test_mode active - random predictions)

**Note**: Keep this terminal open!

### 4. ngrok Tunnel [Running...]

### 4. Start ngrok Tunnel [ ] 
**New Terminal** (keep app.py running)
```bash
./ngrok.exe http 5000
```
Expected: https://*.ngrok-free.app URL – copy this!

### 5. Deploy Frontend to Netlify [ ] 
- Go https://netlify.com
- Sign up/login (GitHub/Google)
- 'Add new site' → 'Deploy manually'
- Drag entire `d:/dl ssa` folder
- Note the deploy URL

### 6. Set Environment Variable [ ] 
- Netlify Dashboard → Site settings → Build & deploy → Environment
- Add: Key=`FLASK_API_URL` Value=`your-ngrok-url`
- 'Save' → Deploys → 'Trigger deploy'

### 7. Test Live Link [ ] 
- Open Netlify URL
- Upload face image
- Predict → emotion result!

**Keep app.py + ngrok running for live backend.**

**Done?** Mark complete, share Netlify link.

**Updated: [Current step here]**
