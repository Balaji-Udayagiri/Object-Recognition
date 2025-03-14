# Object Recognition

This repository is a part of the solution for Object Recognition Hackathon by Northrop Grumman. The contributors of this project are Yashita Watchpillai, Ved Naik, Kapil Rathod and myself (Balaji Udayagiri). This solution secured us the second place in the hackathon.

In this we used a combintation YOLOv7 and Grounding DINO. Used mIOU of the bounding boxes and the Confidence Scores to choose between the YOLOv7 and the Grounding DINO.

# Object Detection Web Application

This project provides two main functionalities:

1.  **Image Upload and Object Detection:** Allows users to upload an image, select a detection model, and view the detected objects with bounding boxes.
2.  **Real-Time Object Detection:** Captures the user's webcam feed and displays real-time object detection with bounding boxes.

## Files

* `upload-image.py`: Handles image uploads, model selection, and object detection on static images.
* `real-time.py`: Processes real-time webcam video streams for object detection.

## Setup

1.  **Clone the Repository:**
    ```bash
    git clone github.com/Balaji-Udayagiri/Object-Recognition.git
    cd Object-Recognition
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Backend Services:**

    * For image uploads:
        ```bash
        python upload-image.py
        ```
    * For real-time detection:
        ```bash
        python real-time.py
        ```
4.  **Access the Web Application:**
    * Open your web browser and navigate to the appropriate URL (usually `http://localhost:<port>`). The port number will be shown when you run the python files.

## Usage

* **Image Upload:**
    1.  Select an image file.
    2.  Choose a detection model.
    3.  Click "Upload" or a similar button.
    4.  View the image with bounding boxes.

![Image Upload Interface](static\images\image-upload.jpeg)

* **Real-Time Detection:**
    1.  Grant webcam access when prompted.
    2.  View the live video feed with real-time bounding boxes.

![Real-Time Interface](static\images\real-time.jpeg)

## Example Results (Image Upload)

Here is an example of images processed by the object detection functionality, showing a comparison between YOLOv7's output and a combined output.


| YOLOv7 Output | Combined Output |
|---|---|
| ![YOLOv7 Result 1](static\images\Picture2.jpg) | ![Combined Result 1](static\images\Picture1.jpg) |

## `.gitignore`

The following files and directories are ignored by Git:
.