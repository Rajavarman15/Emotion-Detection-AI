from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import cv2
import logging
import os

# Try to import TensorFlow, fallback to mock if not available
try:
    from tensorflow.keras.models import load_model
    TENSORFLOW_AVAILABLE = True
except Exception as e:
    print(f"Note: TensorFlow not fully available: {e}")
    print("Using mock predictions for testing...")
    TENSORFLOW_AVAILABLE = False
    load_model = None

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for frontend requests
CORS(app, resources={
    r"/predict": {
        "origins": ["*"],
        "methods": ["POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    },
    r"/health": {
        "origins": ["*"],
        "methods": ["GET", "OPTIONS"]
    }
})

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Emotion labels
EMOTION_LABELS = ["Angry", "Happy", "Sad", "Surprise", "Neutral", "Fear", "Disgust"]

# Model path
MODEL_PATH = "emotion_model.h5"

# Load the pre-trained model
model = None
if TENSORFLOW_AVAILABLE:
    try:
        model = load_model(MODEL_PATH)
        logger.info(f"Model loaded successfully from {MODEL_PATH}")
    except Exception as e:
        logger.warning(f"Failed to load model: {e}")
        logger.warning("Running in TEST MODE with mock predictions")
        model = None
else:
    logger.warning("TensorFlow not available - running in TEST MODE with mock predictions")
    logger.warning("For production, install: pip install tensorflow")


@app.route('/predict', methods=['POST'])
def predict_emotion():
    """
    Predict emotion from an uploaded image.
    
    Expected input:
    - form-data with key "image" containing an image file
    
    Returns:
    - JSON with predicted emotion and confidence score
    """
    try:
        # Check if image is in request
        if 'image' not in request.files:
            return jsonify({'error': 'Missing image file. Please provide an image with key "image"'}), 400
        
        file = request.files['image']
        
        # Check if file is empty
        if file.filename == '':
            return jsonify({'error': 'Empty image file'}), 400
        
        # Check if file has valid image extension
        if not is_valid_image_file(file.filename):
            return jsonify({'error': 'Invalid image format. Allowed: png, jpg, jpeg, gif, bmp'}), 400
        
        # Read and decode image
        try:
            image_data = file.read()
            image_array = np.frombuffer(image_data, np.uint8)
            image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
            
            if image is None:
                return jsonify({'error': 'Failed to decode image. Please ensure it is a valid image file'}), 400
            
        except Exception as e:
            logger.error(f"Error reading image: {str(e)}")
            return jsonify({'error': 'Failed to process image file'}), 400
        
        # Preprocess image
        try:
            processed_image = preprocess_image(image)
        except Exception as e:
            logger.error(f"Error preprocessing image: {str(e)}")
            return jsonify({'error': 'Failed to preprocess image'}), 400
        
        # Make prediction
        try:
            if model is not None:
                # Use real model
                predictions = model.predict(processed_image, verbose=0)
            else:
                # Use mock predictions for testing
                logger.info("Using mock predictions (TEST MODE)")
                predictions = np.random.dirichlet(np.ones(7), size=1)
            
            emotion_index = np.argmax(predictions[0])
            emotion = EMOTION_LABELS[emotion_index]
            confidence = float(predictions[0][emotion_index])
            
            return jsonify({
                'emotion': emotion,
                'confidence': round(confidence, 4),
                'test_mode': model is None
            }), 200
            
        except Exception as e:
            logger.error(f"Error making prediction: {str(e)}")
            return jsonify({'error': 'Failed to make emotion prediction'}), 500
    
    except Exception as e:
        logger.error(f"Unexpected error in predict_emotion: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify API and model status.
    
    Returns:
    - JSON with API status and model status
    """
    model_status = 'loaded' if model is not None else 'test_mode'
    return jsonify({
        'status': 'healthy',
        'model_status': model_status,
        'mode': 'production' if model is not None else 'test',
        'emotions': EMOTION_LABELS
    }), 200


def preprocess_image(image):
    """
    Preprocess image for model input.
    
    Steps:
    1. Convert BGR to grayscale
    2. Resize to 48x48 pixels
    3. Normalize pixel values by dividing by 255.0
    4. Reshape to (1, 48, 48, 1) for model input
    
    Args:
        image: OpenCV image array (BGR format)
    
    Returns:
        Preprocessed image array with shape (1, 48, 48, 1)
    """
    # Convert BGR to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Resize to 48x48 pixels
    resized_image = cv2.resize(gray_image, (48, 48))
    
    # Normalize pixel values to range [0, 1]
    normalized_image = resized_image.astype('float32') / 255.0
    
    # Reshape to (1, 48, 48, 1) for model input
    processed_image = normalized_image.reshape(1, 48, 48, 1)
    
    return processed_image


def is_valid_image_file(filename):
    """
    Validate if file has a supported image extension.
    
    Args:
        filename: Name of the file to validate
    
    Returns:
        True if file has a valid image extension, False otherwise
    """
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}
    if '.' not in filename:
        return False
    
    file_extension = filename.rsplit('.', 1)[1].lower()
    return file_extension in allowed_extensions


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 errors."""
    return jsonify({'error': 'Method not allowed'}), 405


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    # Run Flask app on localhost:5000 with debug mode enabled
    app.run(host='localhost', port=5000, debug=True)
