"""
Quick test script to verify emotion detection is working locally.
"""

import requests
import os
from pathlib import Path

def test_emotion_detection():
    """Test the emotion detection API locally."""
    
    API_URL = "http://localhost:5000/predict"
    
    print("=" * 60)
    print("🧪 EMOTION DETECTION - LOCAL TEST")
    print("=" * 60)
    
    # Test 1: Health check
    print("\n1️⃣  Testing Health Check...")
    try:
        response = requests.get("http://localhost:5000/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Backend Status: {data['status']}")
            print(f"✓ Model Status: {data['model_status']}")
            print(f"✓ Mode: {data['mode']}")
            print(f"✓ Supported Emotions: {', '.join(data['emotions'])}")
        else:
            print("✗ Health check failed!")
            return
    except Exception as e:
        print(f"✗ Error connecting to backend: {e}")
        print("   Make sure Flask is running: python app.py")
        return
    
    # Test 2: Emotion prediction with test image
    print("\n2️⃣  Testing Emotion Prediction...")
    
    # Try to find a test image
    test_image_path = None
    possible_paths = [
        Path.cwd() / "test_image.jpg",
        Path.cwd() / "test.jpg",
        Path.home() / "Pictures" / "test.jpg",
    ]
    
    for path in possible_paths:
        if path.exists():
            test_image_path = path
            break
    
    if test_image_path:
        print(f"   Using test image: {test_image_path}")
        try:
            with open(test_image_path, 'rb') as f:
                files = {'image': f}
                response = requests.post(API_URL, files=files)
            
            if response.status_code == 200:
                data = response.json()
                emotion = data.get('emotion', 'Unknown')
                confidence = data.get('confidence', 0)
                test_mode = data.get('test_mode', False)
                
                print(f"✓ Emotion Detected: {emotion}")
                print(f"✓ Confidence: {confidence*100:.1f}%")
                if test_mode:
                    print("ℹ️  (Using test mode - random predictions)")
            else:
                print(f"✗ Prediction failed: {response.status_code}")
                print(f"   Error: {response.json()}")
        except Exception as e:
            print(f"✗ Error during prediction: {e}")
    else:
        print("   ⚠️  No test image found")
        print("   To test with an image, provide a test image in the current directory")
        print("\n   Upload an image using the web interface instead:")
        print("   📁 Open: d:/dl ssa/index.html")
        print("   🖱️  Drag and drop an image")
        print("   ▶️  Click 'Predict Emotion'")
    
    # Test 3: Missing image (error handling)
    print("\n3️⃣  Testing Error Handling (missing image)...")
    try:
        files = {'wrong_key': ('test.jpg', b'fake_image_data')}
        response = requests.post(API_URL, files=files)
        
        if response.status_code == 400:
            data = response.json()
            print(f"✓ Error handling works: {data.get('error', 'Error message')}")
        else:
            print(f"✗ Unexpected status code: {response.status_code}")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    print("\n" + "=" * 60)
    print("✅ LOCAL TESTING COMPLETE!")
    print("=" * 60)
    print("\n📋 Next Steps:")
    print("1. ✓ Backend running locally")
    print("2. ✓ Frontend ready at d:/dl ssa/index.html")
    print("3. 👉 NEXT: Deploy to Netlify (see NETLIFY_DEPLOYMENT.md)")
    print("\n")

if __name__ == '__main__':
    test_emotion_detection()
