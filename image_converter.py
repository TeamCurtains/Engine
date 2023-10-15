import numpy
from PIL import Image


def cv2_to_pil(cv2_image):
    return Image.fromarray(cv2_image)


def pil_to_cv2(pil_image):
    return numpy.array(pil_image)


def pdfplumber_to_cv2(pdfplumber_image):
    return pil_to_cv2(pdfplumber_image.original)
