# Face Detection using OpenCV and PIL


This Python script detects faces in an image using OpenCV's pre-trained face cascade classifier. It draws rectangles around the detected faces and displays the result using the PIL library.

## Demo

![Screenshot from 2023-08-23 19-54-37](https://github.com/mdjamilkashemporosh/FaceDetectify/assets/50365984/4525e10d-2f07-4663-ae61-bf2a4c92629e)


## Prerequisites

- Python 3. (The code is compatible with Python 3.6 or higher)
- OpenCV (Install using pip install opencv-python)
- Pillow (Install using pip install pillow)

## Getting Started

Clone the repository or download the script file (face_detection.py) to your local machine.
Ensure that the required Python packages (OpenCV and Pillow) are installed. You can install them by running the following commands:

```
pip install opencv-python
pip install pillow
```
or 

```
pip install -r requirements.txt
```
Place the image you want to detect faces in the images folder. Make sure the image file is in a supported format (e.g., JPEG, PNG).
Update the image_path variable in the script (index.py) to the path of your image file ( on line 8 ). For example:

```
image = cv2.imread('images/image_multi.jpg')
```

Run the script using the following command: ```python index.py```.

## Contributing

If you would like to contribute to this web application, please open an issue on GitHub to discuss your ideas or proposed changes. Pull requests are also welcome.

## License

This drawing web application is available under the MIT License. You are free to use, modify, and distribute this project as you see fit.
