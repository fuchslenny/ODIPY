import cv2
from processing import get_input
from processing.helper import check

def main():
    print("Welcome to ODIPY")
    #check if there are cams to use
    is_cam = check.look_for_cams()

    if is_cam == True:
        #pass a None path to check
        get_input.getter(path=None)

    else:
        get_input.path_input()


if __name__ == "__main__":
    main()
