import constants
import image_converter
import pdf_to_image
import tesseract_recognition
import text_detector


def process_document(doc_in):
    page_images_pdf = pdf_to_image.read(doc_in)
    extracted_data = []

    for page_image_pdf_i in range(0, len(page_images_pdf)):
        page_image = image_converter.pdfplumber_to_cv2(page_images_pdf[page_image_pdf_i])
        containers = text_detector.find_containers(page_image, constants.detection_threshold)

        for x in range(0, len(containers)):
            if len(containers[x]) == 0:
                continue
            text = tesseract_recognition.get_text(containers[x])

            for find_character, replace_character in [("{", "("), ("}", ")"), ("\n", " ")]:
                text = text.replace(find_character, replace_character)

            if not "|" in text:
                extracted_data.append((page_image_pdf_i, x, text))

    return extracted_data
