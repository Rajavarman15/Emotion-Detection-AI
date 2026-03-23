// Configuration file for Emotion Detection API

// Determine the backend URL based on environment
function getBackendURL() {
    // In production (Netlify), use the Netlify function proxy
    if (window.location.hostname !== 'localhost' && window.location.hostname !== '127.0.0.1') {
        return `${window.location.origin}/api/predict`;
    }
    
    // In local development, connect directly to Flask
    return 'http://localhost:5000/predict';
}

const CONFIG = {
    // Backend API endpoint for emotion prediction
    API_PREDICT_ENDPOINT: getBackendURL(),
    
    // Supported image types
    SUPPORTED_IMAGE_TYPES: ['image/png', 'image/jpeg', 'image/gif', 'image/bmp'],
    
    // Maximum file size (10MB)
    MAX_FILE_SIZE: 10 * 1024 * 1024,
    
    // Emotion emoji mapping
    EMOTION_EMOJIS: {
        'Angry': '😠',
        'Happy': '😊',
        'Sad': '😢',
        'Surprise': '😮',
        'Neutral': '😐',
        'Fear': '😨',
        'Disgust': '🤢'
    },
    
    // API timeout (milliseconds)
    API_TIMEOUT: 30000
};

// Export for use in HTML
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONFIG;
}
