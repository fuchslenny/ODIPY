import cv2
import sys


#checks if tje file is a image or a video
def check_type(image_path):
    #check if its a image
    if image_path.endswith((".jpg", ".png")):
        return True

    #if its not a image format just use the video processing
    elif image_path.endswith((".mp4", ".gif")):
        return False

    else:
        exit(1)


def look_for_cams():
    camera_instance = cv2.VideoCapture()

    if camera_instance is None or not camera_instance.isOpened():
        return False
    else:
        return True
