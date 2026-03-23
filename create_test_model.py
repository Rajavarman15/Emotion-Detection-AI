"""
Create a simple mock emotion detection model for testing purposes.
This is a minimal neural network that can be used to test the Flask app
before deploying with the real model.
"""

import os
import numpy as np

# Try to import tensorflow, but allow graceful failure
try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
    from tensorflow.keras.optimizers import Adam
    
    def create_test_model():
        """Create a simple CNN for emotion detection testing."""
        model = Sequential([
            Conv2D(32, (3, 3), activation='relu', input_shape=(48, 48, 1)),
            MaxPooling2D((2, 2)),
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Conv2D(64, (3, 3), activation='relu'),
            Flatten(),
            Dense(64, activation='relu'),
            Dense(7, activation='softmax')  # 7 emotions
        ])
        
        model.compile(
            optimizer=Adam(),
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        
        return model
    
    if __name__ == '__main__':
        print("Creating test emotion model...")
        model = create_test_model()
        
        # Save model
        model.save('emotion_model.h5')
        print("✓ Test model saved as emotion_model.h5")
        print(f"Model shape: input (48, 48, 1) → output 7 emotions")
        
except ImportError:
    print("TensorFlow not available. Run: pip install tensorflow")
    print("Using this script to create mock model for testing.")
