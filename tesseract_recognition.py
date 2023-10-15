import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def get_text(img_in):
    # Adding custom options
    custom_config = r'--oem 1 --psm 6'

    return pytesseract.image_to_string(img_in, config=custom_config, lang="rus")
