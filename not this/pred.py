import os
from ultralytics import YOLO
import cv2

def prediction(image):
 #image_path = 'images.jpeg'  # Replace with the actual path to your image
 #output_path = 'output.jpg'  # Specify the output path for the annotated image

# Load the YOLO model
 model_path = r'C:\Users\dell\Desktop\PROJET\runs\detect\train6\weights\best.pt'
 model = YOLO(model_path)

# Read the input image
 #image = cv2.imread(image_path)

# Perform inference on the image
 results = model(image)[0]

# Set a confidence threshold for visualization
 threshold = 0.5

# Process detection results and draw bounding boxes
 for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(image, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)


# Save the annotated image
 #cv2.imwrite(output_path, image)

# Display the annotated image (optional)
 cv2.imshow('Annotated Image', image)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
