import document_processor
import value_matcher

image_file = input("Enter file path")

processed = document_processor.process_document(image_file)
res = []

for x in processed:
    res.append(x[2])
    print(x)

for x in range(0, len(res)):
    print(value_matcher.apply_matcher(res, x))
