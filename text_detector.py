import random

import cv2

import constants


def find_containers(image_in, detection_threshold):
    containers = []

    gray = cv2.cvtColor(image_in, cv2.COLOR_BGR2GRAY)
    thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)[1]

    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (detection_threshold + 10, detection_threshold))
    dilation = cv2.dilate(thresh1, rect_kernel, constants.detector_iterations)

    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    image_copy = image_in.copy()
    for cnt_i in range(0, len(contours)):
        x, y, w, h = cv2.boundingRect(contours[cnt_i])
        cv2.rectangle(image_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cropped = image_in[y:y + h, x:x + w]

        containers.append(cropped)

    return containers
