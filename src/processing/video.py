import cv2
import sys
from src.detection import detect


def get_frames(path):

    if path is None:
        instance = cv2.VideoCapture(path)

    if path != "" or is None:
        instance = cv2.VideoCapture()

    try:
        if !instance.isOpened():
            exit(1)

        while instance.isOpened():
            ret, frame = instance.read()

            if ret == False:
                break

            detect.detect(frame)

    except Exception as e:
        print(e)
        exit(1)
