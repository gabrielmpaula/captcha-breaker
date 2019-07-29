from PIL import Image
import pytesseract
import processing
import argparse

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

parser = argparse.ArgumentParser(description='Break captcha into text.')
parser.add_argument('--filter', dest='pass_factor', default=130,
                   help='define the pass factor of the filter')
parser.add_argument('--file', dest='image_file', default='../input/captcha.jpg',
                   help='define the pass factor of the filter')

args = parser.parse_args()


if __name__ == '__main__':
    args = parser.parse_args()
    image_file = args.image_file
    pass_factor = args.pass_factor
    raw_image = Image.open(image_file)
    processed_image = processing.prepare_image(raw_image)
    processed_image = processing.remove_noise(processed_image, pass_factor)
    captcha_text = pytesseract.image_to_string(processed_image)
    print(f"Captcha text: {captcha_text}")