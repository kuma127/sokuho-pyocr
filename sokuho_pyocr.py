from PIL import Image
import sys
sys.path.append('/path/to/dir')

import pyocr
import pyocr.builders

def print_ocr(img_path,tesseract_layout=3):
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    tool = tools[0]

    txt = tool.image_to_string(
        Image.open(img_path),
        lang='jpn',
        builder=pyocr.builders.TextBuilder(tesseract_layout=tesseract_layout)
    )
    print(txt)

