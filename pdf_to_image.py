import pdfplumber


def read(doc_path) -> list:
    pdf_obj = pdfplumber.open(doc_path)
    res = []

    for page in pdf_obj.pages:
        image_obj = page.to_image(resolution=400)
        res.append(image_obj)

    return res
