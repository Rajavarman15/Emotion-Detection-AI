"""
Create a mock emotion detection model for testing.
This allows testing the Flask app without TensorFlow.
"""

import numpy as np
import json
import os

class MockEmotionModel:
    """Mock model that returns random predictions."""
    
    def __init__(self):
        self.emotions = ["Angry", "Happy", "Sad", "Surprise", "Neutral", "Fear", "Disgust"]
    
    def predict(self, image_array, verbose=0):
        """Return mock predictions."""
        # Return random probabilities for 7 emotions
        predictions = np.random.dirichlet(np.ones(7), size=1)
        return predictions
    
    def save(self, filename):
        """Save mock model info."""
        with open(filename.replace('.h5', '.json'), 'w') as f:
            json.dump({'type': 'mock_emotion_model', 'emotions': self.emotions}, f)

# Create and save mock model
if __name__ == '__main__':
    print("Creating mock emotion model for testing...")
    model = MockEmotionModel()
    
    # Create a marker file
    with open('emotion_model.h5.mock', 'w') as f:
        f.write("This is a mock model for testing\n")
        f.write("Emotions: Angry, Happy, Sad, Surprise, Neutral, Fear, Disgust\n")
    
    print("✓ Created emotion_model.h5.mock")
    print("Note: This is a mock model for testing only.")
