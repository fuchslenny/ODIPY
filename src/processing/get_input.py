import cv2
import sys
from processing.helper import check


def path_input():
    try:
        path = str(input())
    except KeyboardInterrupt:
        exit(1)
        
    is_type = check.check_type(path)

    if is_type == 1:
        input_image = cv2.imread(path)

        if image.empty():
            exit(1)

        frames.append(input_image)

    elif is_type == 0:
        getter(path)


#interface for videos and camera VideoCapture
def getter(path):
    get_frames(path)
