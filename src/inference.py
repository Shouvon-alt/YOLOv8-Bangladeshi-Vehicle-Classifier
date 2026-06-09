```python
from ultralytics import YOLO
import os

MODEL_PATH = "model/best.pt"

def main():
    # Check model exists
    if not os.path.exists(MODEL_PATH):
        print(f"Error: Model not found at {MODEL_PATH}")
        return

    # Get image path
    image_path = input("Enter image path: ").strip()

    # Check image exists
    if not os.path.exists(image_path):
        print("Error: Image file not found.")
        return

    # Load model
    model = YOLO(MODEL_PATH)

    # Predict
    results = model.predict(
        source=image_path,
        save=True,
        conf=0.25
    )

    # Print prediction
    for result in results:
        probs = result.probs

        if probs is not None:
            class_id = probs.top1
            confidence = probs.top1conf.item()

            print(f"\nPredicted Class: {result.names[class_id]}")
            print(f"Confidence: {confidence:.2%}")

if __name__ == "__main__":
    main()
```
