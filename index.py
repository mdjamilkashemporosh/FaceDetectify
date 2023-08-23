import cv2
from PIL import Image

# Load the pre-trained face cascade classifier
face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')

# Read the image file
image = cv2.imread('images/image_multi.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the grayscale image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Define a list of bright colors for drawing rectangles around the faces
colors = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255)]

# Check if any faces are detected
if len(faces) > 0:
    for i, (x, y, w, h) in enumerate(faces):
        # Select a color from the list based on the index
        color = colors[i % len(colors)]
        
        # Draw a rectangle around the face
        cv2.rectangle(image, (x, y), (x+w, y+h), color, 2)
else:
    print("No faces detected.")

# Convert the OpenCV BGR image to PIL RGB image
pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

# Display the image using PIL
pil_image.show()

# Wait for the user to close the image
input("Press any key to close the image...")