@echo off
REM Quick GitHub setup script for Emotion Detection

echo.
echo ========================================
echo GitHub Setup for Emotion Detection
echo ========================================
echo.

REM Initialize Git
echo 1. Initializing Git repository...
git init

REM Add all files
echo 2. Adding all files to Git...
git add .

REM Create commit
echo 3. Creating initial commit...
git commit -m "Initial emotion detection app - ready for Netlify"

REM Display instructions
echo.
echo ========================================
echo Next Steps:
echo ========================================
echo.
echo 1. Create a NEW repository on GitHub:
echo    👉 https://github.com/new
echo.
echo 2. Copy the repository URL from GitHub
echo.
echo 3. Run these commands:
echo    git branch -M main
echo    git remote add origin [PASTE_YOUR_GITHUB_URL]
echo    git push -u origin main
echo.
echo Example (don't paste this!):
echo    git remote add origin https://github.com/yourusername/emotion-detection.git
echo    git push -u origin main
echo.
echo ========================================
